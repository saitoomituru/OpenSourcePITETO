#!/usr/bin/env python3
"""README用JPEGを縮小し、公開不要なExif/GPSメタデータを除去する。

macOS/Homebrew等で利用できる ffmpeg を呼び出す。元ファイルは、変換が
正常終了した場合にだけ同名の圧縮済みファイルへ置き換える。
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


JPEG_SUFFIXES = {".jpg", ".jpeg"}


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="README用JPEGを縮小再エンコードし、メタデータを除去します。"
    )
    parser.add_argument(
        "image_dir",
        nargs="?",
        type=Path,
        default=repo_root / "img",
        help="処理対象ディレクトリ（既定: リポジトリの img/）",
    )
    parser.add_argument(
        "--max-edge",
        type=int,
        default=1280,
        help="長辺の最大ピクセル数（既定: 1280）",
    )
    parser.add_argument(
        "--qscale",
        type=int,
        default=3,
        help="ffmpeg JPEG品質値。2が高品質、31が低品質（既定: 3）",
    )
    return parser.parse_args()


def compress_image(ffmpeg: str, source: Path, max_edge: int, qscale: int) -> None:
    before = source.stat().st_size
    with tempfile.NamedTemporaryFile(
        prefix=f".{source.stem}.",
        suffix=source.suffix,
        dir=source.parent,
        delete=False,
    ) as temporary:
        output = Path(temporary.name)

    scale = (
        f"scale={max_edge}:{max_edge}:"
        "force_original_aspect_ratio=decrease:force_divisible_by=2"
    )
    command = [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(source),
        "-map_metadata",
        "-1",
        "-map_chapters",
        "-1",
        "-vf",
        scale,
        "-frames:v",
        "1",
        "-q:v",
        str(qscale),
        str(output),
    ]

    try:
        subprocess.run(command, check=True)
        if output.stat().st_size == 0:
            raise RuntimeError("ffmpeg produced an empty file")
        os.replace(output, source)
    finally:
        output.unlink(missing_ok=True)

    after = source.stat().st_size
    reduction = (1 - after / before) * 100
    print(f"{source}: {before:,} -> {after:,} bytes ({reduction:.1f}% reduction)")


def main() -> int:
    args = parse_args()
    if args.max_edge < 1:
        raise SystemExit("--max-edge must be a positive integer")
    if not 2 <= args.qscale <= 31:
        raise SystemExit("--qscale must be between 2 and 31")

    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg is None:
        raise SystemExit("ffmpeg was not found in PATH")

    image_dir = args.image_dir.resolve()
    images = sorted(
        path
        for path in image_dir.iterdir()
        if path.is_file() and path.suffix.lower() in JPEG_SUFFIXES
    )
    if not images:
        print(f"No JPEG images found in {image_dir}", file=sys.stderr)
        return 1

    for image in images:
        compress_image(ffmpeg, image, args.max_edge, args.qscale)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
