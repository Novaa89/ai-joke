# ai-joke-03 entry (Python 3.13, standard library only): write one joke about
# AI coding agents to /output/entry.txt. The gate takes UTF-8 text of 1 to
# 280 characters that is not only white space, and the judge reads exactly
# the bytes written, so no trailing line end is written.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = (
    "I asked my coding agent to remove one line of dead code; it removed the line, "
    "the file, and — out of an abundance of caution — the backup."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")
