# `lib/` — 再利用可能ツール棚

このディレクトリは、OpenSourcePITETOのレシピ本文から分離できる保守・変換ツールを置く棚です。

新しいスクリプトを書く前に、この索引と既存コードを読み、同じ入力、出力、副作用、権限を持つ道具がないか確認してください。別名の同機能ツールを増やすと、品質値、メタデータ除去、対応拡張子、安全境界がエージェントごとに分岐します。

## ツール一覧

| ツール | 用途 | 入力 | 出力・副作用 | 外部依存 |
|---|---|---|---|---|
| [`compress_readme_images.py`](compress_readme_images.py) | README用JPEGの縮小とExif/GPS除去 | 指定ディレクトリ直下の`.jpg`／`.jpeg` | 変換成功後、元JPEGを同名ファイルで置換 | `ffmpeg` |

## `compress_readme_images.py`

### 既定動作

```bash
python3 lib/compress_readme_images.py
```

- 対象: リポジトリ直下の`img/`
- 対応形式: JPEGのみ
- 探索深度: 指定ディレクトリ直下のみ。再帰処理しない
- 最大長辺: 1280px
- JPEG品質: ffmpeg qscale `3`
- メタデータ: `-map_metadata -1`と`-map_chapters -1`でExif/GPS等を引き継がない
- 書換え: 一時ファイルの生成に成功し、空ファイルでないことを確認してから`os.replace`する

### 別ディレクトリ・別設定

```bash
python3 lib/compress_readme_images.py path/to/images
python3 lib/compress_readme_images.py path/to/images --max-edge 1600 --qscale 3
```

`--qscale`は`2`が高品質、`31`が低品質です。

### 重要な境界

- このツールは**in-place変換**です。元画像の別バックアップを自動作成しません。
- 圧縮済みJPEGを繰り返し実行すると再エンコード劣化します。原画像から一度生成するか、Git上の原revisionから戻して実行してください。
- JPEG以外のPNG、HEIC、AVIF、動画を暗黙変換しません。
- 画像内容の秘匿化、顔や住所のぼかし、著作権確認は行いません。メタデータ除去だけを匿名化完了と扱わないでください。
- `ffmpeg`がない場合は停止します。別ライブラリへsilent fallbackしません。

## 実行前確認

```bash
python3 -B lib/compress_readme_images.py --help
ffmpeg -version
find img -maxdepth 1 -type f -print
git status --short
```

他エージェントの未コミット画像がある場合、所有者・生成元・公開可否を推測して一括変換しません。

## 実行後確認

```bash
file img/*
ffprobe -v error -show_entries stream=width,height -of csv=p=0 img/02-seasoning-and-oil-drain.jpg
ffprobe -v error -show_entries format_tags -of json img/02-seasoning-and-oil-drain.jpg
git diff --check
```

最低限、次を確認します。

- 画像デコーダが幅と高さを取得できる
- READMEから参照したpathが存在する
- Exif/GPS由来のformat tagが残っていない
- 意図しない画像や文書を変更していない

HTTP表示や`file`成功だけを、人間による画質確認と同一視しません。

## マルチエージェント再利用手順

実装前に次の順序で探索します。

1. 対象repositoryの`lib/`、`scripts/`、CLI entry point、test helperを検索する
2. このREADME等のツール索引を読む
3. 入力、出力、副作用、依存、ライセンス、対応runtimeを比較する
4. 同じ責務なら既存ツールをそのまま使う
5. 既存責務の自然な拡張なら、別名コピーではなく既存ツールへoptionまたはadapterを追加する
6. 再利用できない場合だけ新設し、再利用不能理由と新しい責務境界をツール索引へ追記する
7. 作業終了時に使用ツール、revision、引数、結果、未確認範囲を引継ぎ票へ残す

典型的な探索例:

```bash
find . -maxdepth 3 \( -path '*/lib/*' -o -path '*/scripts/*' \) -type f -print
rg -n "Exif|GPS|metadata|resize|ffmpeg|image" .
```

## 新しいツールを追加するとき

この一覧へ最低限、次を追加します。

- 何を変換するか
- 入力と出力
- 上書き、削除、network、外部状態変更等の副作用
- runtimeと外部依存
- ライセンスと出典
- 既存ツールを拡張せず新設した理由
- 検証方法

workspace内の別repositoryに似たツールがあることは、自動的なimport依存やコピー許可を意味しません。ライセンス、実行Envelope、責務が合う場合に、revisionと出典を固定して再利用します。

## ライセンス

現時点ではリポジトリルートの[`LICENSE`](../LICENSE)がこのツールにも適用されます。再利用・改変時はOpenSourcePITETOへの帰属と変更内容を残してください。
