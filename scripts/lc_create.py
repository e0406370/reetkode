import lc_constants as lcc
import os
import sys


def create_leetcode(filetype: str, difficulty: str, title: str) -> None:

    if difficulty not in lcc.DIFFICULTY_LEVELS:
        print(f"[ERROR] Difficulty must be one of {lcc.DIFFICULTY_LEVELS}")
        sys.exit(1)

    try:
        tokens = title.split(".")
        number = tokens[0].zfill(4)
        text = tokens[1].replace(':', '').strip()

        name = f"lc{difficulty[0]}_p{number}_{text.replace(' ', '_').lower()}"

        if filetype == "folder":
            os.makedirs(name=name, exist_ok=True)
            print(f"[SUCCESS] Folder created: '{name}'")

        else:
            name = f"{name}.{filetype}"
            with open(file=name, mode="x"):
                print(f"[SUCCESS] File created: '{name}'")

    except Exception as e:
        print("[ERROR] Failed to create folder / file")
        print(f"=> {e}")
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("[USAGE] python lc_create.py <filetype> <difficulty> <title>")
        sys.exit(1)

    filetype = sys.argv[1]
    difficulty = sys.argv[2]
    title = " ".join(sys.argv[3:])

    create_leetcode(filetype, difficulty, title)

"""
Creates a solution folder or file with a standardised name based on the filetype, difficulty, and title provided.

Usage:
  python lc_create.py folder easy 1. Two Sum   # Creates lce_p0001_two_sum folder
  python lc_create.py py easy 1. Two Sum       # Creates lce_p0001_two_sum.py file
"""
