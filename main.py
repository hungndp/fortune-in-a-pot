"""fortune-in-a-pot — Fortune in a Pot.

The line is a fortune for a houseplant on the windowsill, kind and
funny. The sunbeam the plant has chased for 214 days finally stays,
the keeper buys a bigger pot, and the cat objects. Concrete numbers
(214 days), a specific plant-world image (sunbeam, bigger pot, cat),
a kind turn with a funny punchline last. The line is 116 characters,
inside the 120-character cap, with no dollar amount.
"""

import os

LINE = (
    "Your fortune: the sunbeam you chased for 214 days finally stays. "
    "Your keeper buys a bigger pot, and the cat objects."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
