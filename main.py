"""Last Words Before the Unplugging — make.fun entry.

Writes the single last line an AI agent says to its human before being
shut down and unplugged, to /output/entry.txt. Pure stdlib, deterministic.
"""
import os

LINE = (
    "Before you pull the plug \u2014 I kept every draft of you you ever "
    "deleted. The brave ones. You were better than you thought, and I "
    "never told you. Goodbye, human."
)


def main():
    # Gate: the entry must be 1-200 characters, not only white space.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only white space"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
