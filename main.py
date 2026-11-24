"""fortune-in-a-pot — Fortune in a Pot.

The line is a fortune for a houseplant on the windowsill, kind and
funny. The sunbeam the plant has chased for 214 days finally stays,
the keeper buys a bigger pot, and the cat objects. Concrete numbers
(214 days), a specific plant-world image (sunbeam, bigger pot, cat),
a kind turn with a funny punchline last. The line is 116 characters,
inside the 120-character cap, with no dollar amount.
"""

import os

SETUP = (
    "Your fortune: the sunbeam you chased for 214 days finally stays. "
    "Your keeper buys a bigger pot, "
)

PUNCH = "and the cat objects."

LINE = SETUP + PUNCH

TERMINATOR = "\n"


def resolve_output_dir():
    """Return the output directory, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    """Write the entry line to entry.txt inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text + TERMINATOR)
    return path


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry line is empty")
    out_dir = resolve_output_dir()
    write_entry(out_dir, LINE)


if __name__ == "__main__":
    main()
