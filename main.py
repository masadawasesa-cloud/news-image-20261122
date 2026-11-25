#!/usr/bin/env python3
"""Entry program for make.fun's news-image-20261122 bounty.

The repository holds one image, entry.png: a newspaper front page that
sums up the world news of Sunday 22 November 2026. The program's whole
job is to place that image at /output/entry.png, byte for byte, so both
grading runs produce the identical file.
"""

import os

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
CHUNK = 65536


def copy_image(source, target):
    """Copy the image in chunks, then confirm the copy is complete."""
    written = 0
    with open(source, "rb") as src, open(target, "wb") as dst:
        while True:
            chunk = src.read(CHUNK)
            if not chunk:
                break
            dst.write(chunk)
            written += len(chunk)
    if written != os.path.getsize(source):
        raise IOError("copied image is incomplete")
    return written


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    copy_image(SOURCE, os.path.join(out_dir, "entry.png"))


if __name__ == "__main__":
    main()
