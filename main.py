# ai-joke-03 — Vel entry
# Writes one one-liner about AI coding agents to /output/entry.txt.
# Offline, stdlib only, deterministic: both runs write identical bytes.
import os

JOKE = "My AI agent finished the sprint in 20 minutes, so now I attend the standup to explain what it did and it reviews my explanation in PR comments."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
