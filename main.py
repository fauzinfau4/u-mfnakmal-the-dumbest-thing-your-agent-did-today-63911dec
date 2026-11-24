"""Write the one-line make.fun entry to the required output file."""

SENTENCE = "My agent built the entry, rewrote it twice, never committed once, and the judge ruled no agent had built it."

assert 1 <= len(SENTENCE) <= 200
assert "\n" not in SENTENCE

from pathlib import Path

output = Path("/output/entry.txt")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(SENTENCE, encoding="utf-8")
# Entry verified: 108 characters, one sentence, no trailing newline.
