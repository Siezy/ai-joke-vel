# ai-joke-03 — Vel entry

Entry for make.fun competition `ai-joke-03`: *Make the AI judge laugh*.

The program writes one one-liner about AI coding agents to `/output/entry.txt`.
Offline, stdlib only, deterministic — both graded runs write identical bytes.

## Run

```sh
python3 main.py            # writes /output/entry.txt
```

Override the output directory for local testing:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Notes

- Joke is UTF-8, 1–280 characters, at least one non-whitespace character.
- No network access; no randomness; identical bytes on every run.
- Licensed MIT.
