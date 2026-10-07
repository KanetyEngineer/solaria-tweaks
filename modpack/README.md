# Solaria SMP 起動構成（.mrpack）

Solaria SMP（Minecraft 1.21.11 / Fabric 0.19.5、接続先 `solaria.asutan.jp`）のクライアント構成です。
Solaria Tweaks・Item Scroller（クラフト修正版）・ゆらもんさんのトーテム／古代の残骸リソースパックを含みます。

## 入れ方（Prism Launcher）
1. [Releases](https://github.com/KanetyEngineer/solaria-tweaks/releases) の `modpack-v*` から `Solaria-SMP-*.mrpack` をダウンロード
2. Prism Launcher の「インスタンスを追加 → インポート」で .mrpack を選ぶ
3. 起動するとマルチプレイの一覧に Solaria SMP が入っています

Modrinth App や ATLauncher など、.mrpack を読めるランチャーでも使えます。

## 中身
- `modrinth.index.json`: MOD とリソースパックの一覧（Modrinth と GitHub Releases のダウンロード先とハッシュ）。MOD 本体は同梱していません
- `overrides/`: 設定（config・options.txt・鯖リスト）、自作のリソースパック、Item Scroller クラフト修正版

リソースパックは「ゆらもんの不死のトーテム」「ゆらもんの古代の残骸」が最初から有効です。いらなければリソースパック画面で外してください。

## 作り直し
Prism のインスタンスを書き出したフォルダから作ります（地図のキャッシュやワールドごとの設定などの個人データは外れます）。

```
python modpack/make_from_instance.py "<インスタンスのフォルダ>" modpack <バージョン>
```

Actions の `modpack` ワークフローを `version` 付きで実行すると、`Solaria-SMP-<version>.mrpack` を作ってリリース `modpack-v<version>` に付けます。
