#!/usr/bin/env python3
"""News-image entry for Tuesday 24 November 2026 (Python 3.13, stdlib only).

The entry is the front-page image stored next to this script: a dense
newspaper page summing up the day in 24 stories, as reported. The lead
story is Huang's return to Nvidia and the Wall Street rally that
followed; the two second stories are the COP31 collapse being denounced
as the worst summit ever and Iran striking Bahrain and tankers in the
Gulf. The image is 1024x1024 and under 1 MiB.

This program places a copy of that image at $MAKEFUN_OUTPUT_DIR/entry.png
(/output by default). Copying is deterministic by construction, so two
runs produce byte-identical output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def _copy_front_page(target_dir: str) -> str:
    origin = os.path.join(SCRIPT_DIR, "entry.png")
    target = os.path.join(target_dir, "entry.png")
    os.makedirs(target_dir, exist_ok=True)
    shutil.copyfile(origin, target)
    return target


def _check_sizes(origin: str, target: str) -> bool:
    expected = os.path.getsize(origin)
    actual = os.path.getsize(target)
    if actual != expected:
        print(
            f"error: wrote {actual} bytes, expected {expected}",
            file=sys.stderr,
        )
        return False
    print(f"{target} {actual} bytes")
    return True


def run() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    origin = os.path.join(SCRIPT_DIR, "entry.png")
    target = _copy_front_page(out_dir)
    if not _check_sizes(origin, target):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(run())
