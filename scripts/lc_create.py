import os
import sys


def create_leetcode(filetype: str, difficulty: str, title: str) -> None:

    valid_difficulties = ["easy", "medium", "hard"]
    if difficulty not in valid_difficulties:
        print(f"[ERROR] Difficulty must be one of {valid_difficulties}")
        sys.exit(1)

    tokens = title.split(".")
    number = tokens[0].zfill(4)
    text = tokens[1].strip()

    name = f"lc{difficulty[0]}_p{number}_{text.replace(' ', '_').lower()}"
    try:
        if filetype == "folder":
            os.makedirs(name=name, exist_ok=True)
            print(f"[SUCCESS] Folder created: {name}")

        else:
            name = f"{name}.{filetype}"
            with open(file=name, mode="x"):
                print(f"[SUCCESS] File created: {name}")

    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 4:
        # Create folder: python lc_create.py folder easy 1. Two Sum => lce_p0001_two_sum
        # Create file:   python lc_create.py py easy 1. Two Sum => lce_p0001_two_sum.py
        print("[USAGE] python lc_create.py <filetype> <difficulty> <title>")
        sys.exit(1)

    filetype = sys.argv[1]
    difficulty = sys.argv[2]
    title = " ".join(sys.argv[3:])

    create_leetcode(filetype, difficulty, title)
