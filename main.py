#!/usr/bin/env python3
"""Copy entry.png to /output/entry.png, byte for byte.

Deterministic: the same input bytes always produce the same output bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"
EXPECTED_SHA256 = "e616de3a368a8e99a161d3f1fa5b7be52127fdf6b426c414a54fc794c7516ddc"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    data = open(DST, "rb").read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print("MISMATCH: wrote %s, expected %s" % (digest, EXPECTED_SHA256),
              file=sys.stderr)
        sys.exit(1)
    print("wrote %s (%d bytes, sha256 %s)" % (DST, len(data), digest))


if __name__ == "__main__":
    main()
