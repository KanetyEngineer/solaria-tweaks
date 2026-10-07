# Solaria SMP 起動構成（.mrpack）

Solaria SMP（Minecraft 1.21.11 / Fabric 0.19.5、接続先 `solaria.asutan.jp`）のクライアント構成です。
Solaria Tweaks・Item Scroller（クラフト修正版）・ゆらもんさんのリソースパック（不死のトーテム・古代の残骸）を含みます。

## 入れ方（Prism Launcher）
1. [Releases](https://github.com/KanetyEngineer/solaria-tweaks/releases) の `modpack-v*` から `Solaria-SMP-*.mrpack` をダウンロード
2. Prism Launcher の「インスタンスを追加 → インポート」で .mrpack を選ぶ
3. 起動するとマルチプレイの一覧に Solaria SMP が入っています

Modrinth App や ATLauncher など、.mrpack を読めるランチャーでも使えます。

## 中身
- `modrinth.index.json`: MOD とリソースパックの一覧（Modrinth と GitHub Releases のダウンロード先とハッシュ）。MOD 本体は同梱していません
- `overrides/`: 設定（config・options.txt・鯖リスト）、ゆらもんパック、Item Scroller クラフト修正版

リソースパック「ゆらもんパック」（不死のトーテムと古代の残骸）が最初から有効です。Respackopts の設定（リソースパック画面の歯車）でトーテムと古代の残骸を個別にオンオフできます。

## 作り直し
Prism のインスタンスを書き出したフォルダから作ります（地図のキャッシュやワールドごとの設定などの個人データは外れます）。

```
python modpack/make_from_instance.py "<インスタンスのフォルダ>" modpack <バージョン>
```

main に入ると Actions の `modpack` ワークフローが `Solaria-SMP-<versionId>.mrpack` を作り、まだ無ければリリース `modpack-v<versionId>` を作ります（新しく出すときは modrinth.index.json の versionId を上げる）。
