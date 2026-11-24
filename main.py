# Ridiculous at First Glance, Real by the Second — the pitch

# A program that writes one original startup pitch to /output/entry.txt —
# an entry for the make.fun bounty
# "Ridiculous at First Glance, Real by the Second"
# (u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a).
# The judge compares pitches pairwise on how bizarre the idea is and
# whether the business logic holds up on a second look.
#
# The pitch: professional apologisers who say sorry to your in-laws for
# you. Bizarre at first glance (who hires someone to apologise?), sound
# on the second (one scripted apology a month saves marriages, and
# subscribers pay to never grovel again). One sentence, 166 characters.

LINE = (
    "We hire professional apologisers to say sorry to your in-laws for you, "
    "because one scripted apology a month saves marriages and subscribers "
    "pay to never grovel again."
)

import os
from pathlib import Path

if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"entry line must be 1-200 characters, got {len(LINE)}")
if LINE.strip() != LINE or "\n" in LINE:
    raise SystemExit("entry line must be a single line with no surrounding whitespace")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
print(f"Wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")
