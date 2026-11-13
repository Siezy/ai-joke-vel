# ai-joke-03 — Vel entry
# Writes one one-liner about AI coding agents to /output/entry.txt.
# Offline, stdlib only, deterministic: both runs write identical bytes.
import os

JOKE = "It wrote a flawless migration, dropped the table, and cited the docs it also wrote."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
