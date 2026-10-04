Solaria SMP（Minecraft 1.21.11 / Fabric）向けの補助 MOD です。

## 添付ファイル
- **solaria-tweaks-1.1.0+mc1.21.11.jar**: サーバーとクライアントの両方に入れます（Fabric API が必要）
- **solaria-carpet-1.0.0+mc1.21.11.jar**: サーバーにだけ入れます（fabric-carpet が必要）

## 1.1.0 の変更点
- **サーバー全体の記録**: `/lb server` で採掘数・プレイ時間・移動距離などの全員の合計と、それぞれの1位を表示します。`/lb show server` でサイドバーにも出せます。各順位表のいちばん上には「サーバー合計」が出ます
- 順位表の項目を追加しました: `travel` 移動距離（すべて）、`bred` 繁殖、`enchant` エンチャント、`chests` チェストを開けた回数、`pvp` プレイヤーを倒した数
- **オブザーバー前の誤設置警告**が Litematica の EasyPlace や Tweakeroo で置く場合にも効くようになりました。右クリックを押しっぱなしにしていると通ってしまう問題も直しました（一度離して押し直すと設置できます）
- **MaLiLib 対応**: MaLiLib が入っていれば、Litematica と同じ形式の設定画面（`Ctrl + B`、Mod Menu からも開けます）とホットキーが使えます
- 画面やメッセージの日本語を見直しました
- ポーション複製と光抑制は、Carpet のルールとして切り替える **Solaria Carpet** に移しました（`/carpet potionDupe true`、`/carpet lightSuppression true`）。光抑制は昔の光抑制装置が使えるように作り直しています

1.0.0 から更新する場合は、サーバーに Solaria Carpet と fabric-carpet も入れてください。設定は `/carpet setDefault potionDupe true` のように保存します。

---

Helper mods for the Solaria SMP (Minecraft 1.21.11, Fabric). Solaria Tweaks (server and clients, needs Fabric API): shared Xaero waypoints, stat leaderboards with server-wide totals (`/lb server`), Syncmatica build plans and an observer misplacement guard that now also stops Litematica Easy Place, with an optional MaLiLib config screen. Solaria Carpet (server only, needs fabric-carpet): Carpet rules `potionDupe` (1.21.1 potion duplication) and `lightSuppression` (makes old light suppressors work again).
