"""One-star cat review: lap occupied by laptop.

Writes exactly one line to /output/entry.txt (no trailing newline).
Stdlib only.
"""

import os

LINE = (
    "\u2605\u2606\u2606\u2606\u2606 My lap has been occupied by a glowing rectangle "
    "for six hours. I pay rent in purrs and still get evicted daily. "
    "The rectangle does not even purr back."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
