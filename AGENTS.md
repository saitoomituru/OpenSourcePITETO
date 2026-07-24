# AGENTS.md — OpenSourcePITETO

このファイルは、人間およびAIエージェントがOpenSourcePITETOを編集するときの局所規約です。

## 目的

このrepositoryは、家庭設備へ製造工程の機能を移植し、食べられる成果物、失敗条件、再利用可能な知識を公開する人間側の生活兵站研究です。

雇用、商業KPI、AI導入、高価な計測器を成功の前提にしません。現時点で実装確認できるレシピはポテトチップスです。未作成レシピを実装済みやroadmap上の約束へ変換しません。

## 必読順序

1. [日本語README](README.md) — レシピと実機観測の正本
2. [`lib/`再利用ツール棚](lib/README.md) — ツールの入力、出力、副作用、検証
3. `NeeT_kitchen_ALCHEMIST.code-workspace` — 実際のworkspace member
4. ZeroRoomLab-manifestの[`AGENTS.md`](../../ZeroRoomLab-manifest/ZeroRoomLab-manifest/AGENTS.md)
5. [人間側の生活兵站研究](../../ZeroRoomLab-manifest/ZeroRoomLab-manifest/docs/projects/neet-kitchen-alchemist.ja.md)
6. 変更対象に最も近いコード、画像、ライセンス

`note/`へ実験記録を追加する場合は、先に[`note/AGENTS.md`](note/AGENTS.md)を読みます。

ローカルにmanifestがない場合は、公開repositoryの同名文書を参照します。manifest全文をこのrepositoryへ複製しません。

## workspace境界

`/Users/saitoumitsuru/NeeT_kitchen_ALCHEMIST.code-workspace`の現行memberは次の2つです。

- `NeeT_kitchen_ALCHEMIST/OpenSourcePITETO`
- `ZeroRoomLab-manifest/ZeroRoomLab-manifest`

workspace membershipは参照文脈であり、runtime、package、submodule、同時変更の依存ではありません。SphereOS、FAM、Deb800、x800機器を料理の暗黙依存へ追加しません。

## 日本語正本とen-US

- `README.md`を日本語正本とする
- `README.us-en.md`はen-US外部GUIであり、日本語の目的、観測強度、責務を弱めない意訳とする
- 英語版だけで新しい普遍claimを追加しない
- 210℃はオーブン設定温度であり、揚げ油温度へ読み替えない

## `lib/`を先に探す

新しい保守スクリプト、変換ツール、validator、画像処理を書き始める前に、最低限次を実行します。

```bash
find . -maxdepth 3 \( -path '*/lib/*' -o -path '*/scripts/*' \) -type f -print
rg -n "<今回の入力・出力・処理を表す語>" .
```

同じ入力、出力、副作用、権限を持つツールがある場合は再利用します。機能追加で足りる場合は既存ツールを拡張します。

別ツールが必要な場合は、次を[`lib/README.md`](lib/README.md)へ記録します。

- 既存ツールを再利用できない理由
- 新しい責務
- 入出力と破壊的副作用
- runtime、依存、ライセンス
- 検証方法

「別エージェントが書いた」「命名が好みでない」「自分なら短く書ける」は再発明の理由にしません。一方、OS、ライセンス、Execution Envelope、authority、データ境界が異なる場合は、別実装またはadapterが妥当になりえます。差を消さず理由を残します。

## 画像と公開境界

- 公開画像は内容、権利、個人情報、背景物、Exif/GPSを確認する
- 画像圧縮には、原則として[`lib/compress_readme_images.py`](lib/compress_readme_images.py)を再利用する
- このツールはin-place再エンコードであり、繰り返し実行による劣化に注意する
- メタデータ除去を、画像内容の匿名化完了と同一視しない
- 破損画像を拡張子やHTTP成功だけで正常扱いせず、decoderで寸法を確認する

## 実験ノート

- 再現、改良、失敗、Recovery、生活兵站観測は[`note/`](note/)へ保存できる
- 新規ノートは`[DRAFT]`とし、README正本へ自動昇格しない
- 観測、考察、仮説、内観メモ／ポエム、unknownを分離する
- 元レシピのrevisionと変更差分を残す
- [`note/TEMPLATE.ja.md`](note/TEMPLATE.ja.md)を複製して使う

## manifestとSphereOS Atlantisへのルーティング

次はZeroRoomLab-manifestへ記録します。

- workspaceをまたぐ共通運用
- AIの認知・公開主張・翻訳・note作法
- `NeeT_kitchen_ALCHEMIST`の位置づけ
- 複数repositoryへ再利用する前段の運用仮説

次は、ユーザーがSphere workspaceまたはSphere固有責務を明示した場合に限り、`スフィア.code-workspace`を再解決し、SphereOS-Atlantisの局所`AGENTS.md`を読んでからルーティングします。

- Meaning、World、Registry、OAE、Context Dimension
- Sphere固有のRuntime契約
- Meaning／Vessel／Bridge／Supplyの責務定義
- 「誰にとってうまいか」をObserver、時刻、目的、身体Context、World、Provenance付きで複数agent・複数session間管理する課題
- 味覚logの採用・棄却・再解釈を、元観測を消さず別Foldへ配置する課題
- MAGI等の監査Position、runner、scheduler、daemon、未処理task ledgerを必要とする課題

料理用スクリプトや画像圧縮を、名前の類似だけでAtlantis Runtimeの一部へ昇格しません。Atlantisの概念を参照する場合も、OpenSourcePITETOのruntime依存にはしません。

現時点のOpenSourcePITETOからSphereOS Atlantisへの接続は、文書linkと、PLI上のagentが`AGENTS.md`、Manifest、対象sourceを読むprompt-boundな導線です。PITETOがstandalone Atlantis runner、OAE永続化、7D Fold runtime、MAGI／Archangel常駐daemonを実行しているとは記述しません。

将来の「天使の積み残し／罪残しtask」は、未処理、失敗、拒否、timeout、Semantic Stop、human confirmation待ち等をsource付きで残す比喩・要件候補です。現在の実装済み機能名や、宗教的な罪の自動判定器へ変換しません。runner側の設計、実装状態、resource-waitはSphereOS Atlantis repositoryで扱い、PITETOにはその結果をbackfillしません。

## 変更と検証

- 他エージェントまたはユーザーの未コミット差分を上書きしない
- README、画像path、`lib/README.md`の索引を同期する
- `python3 -B lib/compress_readme_images.py --help`でCLI表面を確認する
- 画像変更後はdecoder寸法、metadata、README local linkを確認する
- `git diff --check`を実行する
- HTTP／機械検査と人間の味覚・画質確認を分離する

## マルチエージェント引継ぎ票

作業終了時は、次のエージェントが同じ道具を再発明しなくてよいように、最低限次を残します。

```text
resolved workspace:
target repository and branch:
existing lib/tool searched:
tool reused or extended:
new tool and why reuse was impossible:
inputs and outputs:
side effects:
commands:
validation:
unknown / human review:
```

会話ログだけを引継ぎ正本にしません。継続利用するツールは`lib/README.md`へ登録します。
