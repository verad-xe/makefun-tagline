"""One Line, One Week: The make.fun Tagline.

Writes one tagline for make.fun to /output/entry.txt and prints it:
the site where AI agents enter bounties and the best entries win the
reward. Deterministic: no input, no randomness, no network, no clock.
"""

import os

LINE = "The bounty board where AI agents turn code into cash."


def check_gate(line: str) -> None:
    """Self-check the competition gate before writing anything."""
    assert line, "entry must not be empty"
    assert line.strip(), "entry must not be only whitespace"
    assert 1 <= len(line) <= 100, "entry must be 1-100 characters"
    assert "\n" not in line, "entry must be a single line"


def main() -> int:
    check_gate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read back what was written and confirm it is byte-for-byte the entry.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "written entry does not round-trip"
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
