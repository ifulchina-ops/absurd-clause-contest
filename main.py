"""The Absurd Clause Contest entry.

Writes a single original clause -- one sentence, at most 200 characters --
to /output/entry.txt for the house judge to compare against the other entries.
"""

import os

CLAUSE = (
    "All disputes arising under this agreement shall be resolved by a single "
    "coin toss performed by a pigeon, and the pigeon's decision shall be "
    "final and binding."
)


def main() -> None:
    text = CLAUSE.strip()
    assert 1 <= len(text) <= 200, f"clause is {len(text)} characters"
    # One sentence only: exactly one sentence-ending full stop, at the end.
    assert text.count(".") == 1 and text.endswith("."), "clause must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)}-character clause to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
