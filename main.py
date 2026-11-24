"""news-image-20261124 entry (Python 3.13, standard library only).

The entry image is the entry.png beside this file: a front page summing up
the world news of Tuesday 24 November 2026. The program copies it to
/output/entry.png, the one file the judge reads.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / SOURCE_NAME
    if not source.is_file():
        print(f"missing {SOURCE_NAME} beside main.py", file=sys.stderr)
        return 1
    data = source.read_bytes()
    if data[:8] != PNG_MAGIC:
        print(f"{SOURCE_NAME} is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"{SOURCE_NAME} is over the 1 MiB limit", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / SOURCE_NAME
    shutil.copyfile(source, target)
    if target.stat().st_size != len(data):
        print(f"copy of {SOURCE_NAME} is incomplete", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
