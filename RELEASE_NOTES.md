Solaria SMP（Minecraft 1.21.11 / Fabric）向けの補助 MOD です。

## 添付ファイル
- **solaria-tweaks-1.2.0+mc1.21.11.jar**: サーバーとクライアントの両方に入れます（Fabric API が必要）
- **solaria-carpet-1.0.3+mc1.21.11.jar**: サーバーにだけ入れます（fabric-carpet が必要）

## 1.2.0 の変更点
- **フィルター詰め**: ホッパーなどを開くと右側にボタンが出ます。仕分け機のフィルター（1枠目に手に持ったアイテム18個、残りに埋め物1個ずつ）、覚えた配置、Litematica の設計図どおりの中身を、手持ちから自動で詰めます。個数と埋め物は `/filterfill` か MaLiLib の設定画面で変えられます
- **光抑制（Solaria Carpet 1.0.3）の不具合修正**: 光抑制中に新しいチャンクを読み込むとサーバーが固まって落ちる不具合を直しました。処理待ちには上限（`lightSuppressionMaxQueue`、既定 30 万件）を付け、チャンク読み込みで止まる時間を数秒に抑えています。光抑制を切ったあとの処理待ちも、すぐ片付くようにしました
- サーバーのログに出ていた MaLiLib の警告を消しました

## 1.1.0 の変更点
- **サーバー全体の記録**: `/lb server` で採掘数・プレイ時間・移動距離などの全員の合計と、それぞれの1位を表示します。`/lb show server` でサイドバーにも出せます。各順位表のいちばん上には「サーバー合計」が出ます
- 順位表の項目を追加: `travel` 移動距離、`bred` 繁殖、`enchant` エンチャント、`chests` チェストを開けた回数、`pvp` プレイヤーを倒した数
- **オブザーバー前の誤設置警告**が Litematica の EasyPlace や Tweakeroo で置く場合にも効くようになり、押しっぱなしで通ってしまう問題も直しました
- **MaLiLib 対応**: 設定画面（`Ctrl + B`、Mod Menu からも開けます）とホットキー
- ポーション複製と光抑制を Carpet のルール（**Solaria Carpet**）に移しました: `/carpet setDefault potionDupe true`、`/carpet setDefault lightSuppression true`

1.0.0 から更新する場合は、サーバーに Solaria Carpet と fabric-carpet も入れてください。

---

Helper mods for the Solaria SMP (Minecraft 1.21.11, Fabric). Solaria Tweaks (server and clients, needs Fabric API): shared Xaero waypoints, stat leaderboards with server-wide totals (`/lb server`), Syncmatica build plans, an observer misplacement guard that also stops Litematica Easy Place, one-click sorter filter filling for hoppers, and an optional MaLiLib config screen. Solaria Carpet (server only, needs fabric-carpet): Carpet rules `potionDupe` (1.21.1 potion duplication) and `lightSuppression` (makes old light suppressors work again, with a queue cap so chunk loads never hang the server).
