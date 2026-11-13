"""ai-joke-03 entry: writes one fixed joke about AI coding agents.

The joke is deterministic: every run writes the same bytes to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
No network, standard library only.
"""

import os
from pathlib import Path

JOKE = "My AI coding agent's idea of a quick fix is 12 new files, 4 new dependencies and a framework named after itself."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
