"""A childhood memory, written for make.fun's nostalgic AI judge.

The entry is a single sentence about my grandmother's kitchen: the smell of
ginger and coal smoke, and her kind little fib that the first dumpling had
split open — her excuse for letting me eat one before dinner. The program
writes that sentence, unchanged, to /output/entry.txt.
"""

import os

ENTRY = "My grandmother's kitchen smelled of ginger and coal smoke, and she always claimed the first dumpling had split open, so I could eat it before dinner."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"{OUTPUT_PATH}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()
