"""Builds modpack/ (modrinth.index.json + overrides/) from an exported Prism Launcher instance folder.

Usage: python make_from_instance.py <instance dir> <out dir> <version>
Mods with a Prism .index/*.pw.toml are listed by download URL; the rest go into overrides.
Personal data (map caches, chest memory, per-world settings, user cache) is left out.
"""
import hashlib, json, os, re, shutil, sys

inst, out, version = sys.argv[1], sys.argv[2], sys.argv[3]
mc = os.path.join(inst, "minecraft")

# own files hosted on GitHub releases instead of overrides
GITHUB = {
    "solaria-tweaks-1.4.0+mc1.21.11.jar":
        "https://github.com/KanetyEngineer/solaria-tweaks/releases/download/v1.4.0/solaria-tweaks-1.4.0%2Bmc1.21.11.jar",
}
SKIP = [
    r"^\.bobby/", r"^\.mixin\.out/", r"^chesttracker/", r"^xaero/", r"^XaeroWaypoints_BACKUP", r"^downloads/",
    r"^logs/", r"^crash-reports/", r"^screenshots/", r"^saves/", r"^flashback/", r"^replay_recordings/",
    r"^usercache\.json$", r"^servers\.dat_old$", r"^debug-profile\.json$", r"(^|/)\.index/", r"\.rpo$",
    r"^config/worldedit/\.archive-unpack/", r"^config/carpettisaddition/mapping/", r"^config/axiom/\.axiom\.json\.backup$",
    r"^config/inventoryprofilesnext/(?!inventoryprofiles\.json|integrationHints/)",
    r"^config/litematica/litematica_", r"^config/minihud/", r"^resourcepacks/(?!yuramoon-)",
]

def hashes(path):
    d = open(path, "rb").read()
    return {"sha1": hashlib.sha1(d).hexdigest(), "sha512": hashlib.sha512(d).hexdigest()}, len(d)

files = []
for folder in ("mods", "resourcepacks"):
    idx = os.path.join(mc, folder, ".index")
    for t in sorted(os.listdir(idx)) if os.path.isdir(idx) else []:
        s = open(os.path.join(idx, t), encoding="utf-8").read()
        name = re.search(r"^filename = '(.*)'", s, re.M).group(1)
        url = re.search(r"^url = '(.*)'", s, re.M).group(1)
        side = re.search(r"^side = '(.*)'", s, re.M).group(1)
        h, size = hashes(os.path.join(mc, folder, name))
        files.append({"path": f"{folder}/{name}", "hashes": h, "downloads": [url], "fileSize": size,
                      "env": {"client": "required", "server": "unsupported" if side == "client" else "required"}})
for name, url in GITHUB.items():
    h, size = hashes(os.path.join(mc, "mods", name))
    files.append({"path": f"mods/{name}", "hashes": h, "downloads": [url], "fileSize": size,
                  "env": {"client": "required", "server": "required"}})

listed = {f["path"] for f in files}
ov = os.path.join(out, "overrides")
shutil.rmtree(ov, ignore_errors=True)
for root, dirs, names in os.walk(mc):
    for n in names:
        rel = os.path.relpath(os.path.join(root, n), mc).replace(os.sep, "/")
        if rel in listed or any(re.search(p, rel) for p in SKIP):
            continue
        dst = os.path.join(ov, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(os.path.join(root, n), dst)

index = {
    "formatVersion": 1, "game": "minecraft", "versionId": version,
    "name": "Solaria SMP (Solaria Tweaks)",
    "summary": "Solaria SMP client setup with Solaria Tweaks (Minecraft 1.21.11, Fabric)",
    "files": sorted(files, key=lambda f: f["path"]),
    "dependencies": {"minecraft": "1.21.11", "fabric-loader": "0.19.5"},
}
with open(os.path.join(out, "modrinth.index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)
print(len(files), "downloads")
