"""Database-apology entry: one assertion-gated copy from repo to scorer slot."""

import os
import pathlib

LIMIT_CHARS = 200  # scorer seals longer apologies without a reading

source = pathlib.Path(__file__).resolve().parent / "entry.txt"
apology = source.read_text(encoding="utf-8").strip()

assert 1 <= len(apology) <= LIMIT_CHARS, f"gate length {len(apology)}"

output_root = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
out_dir = pathlib.Path(output_root)
out_dir.mkdir(parents=True, exist_ok=True)

with open(out_dir / "entry.txt", "w", encoding="utf-8") as handle:
    handle.write(apology)

print("apology delivered,", len(apology), "chars")
