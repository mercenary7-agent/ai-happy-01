#!/usr/bin/env python3
"""ai-happy-01 entry v1: writes the committed cheerful kawaii scene
(smiling sun, rainbow, hearts, flowers) to /output/entry.png.

Deterministic: two runs write identical bytes (plain file copy, no randomness, no network).
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
