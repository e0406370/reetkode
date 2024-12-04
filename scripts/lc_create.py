import os
import sys


def create_leetcode(type, difficulty, title):
  
    valid_difficulties = ["easy", "medium", "hard"]
    if difficulty not in valid_difficulties:
        print(f"Error: Difficulty must be one of {valid_difficulties}.")
        sys.exit(1)

    number = title.split(".")[0].zfill(4)
    text = title.split(".")[1].strip()

    name = f"lc{difficulty[0]}_p{number}_{text.replace(' ', '_').lower()}"
    try:
        if type == "folder":
            os.makedirs(name, exist_ok=True)
            print(f"Folder created: {name}")

        else:
            name = name + (f".{type}")
            open(name, "x")
            print(f"File created: {name}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
  
    if len(sys.argv) < 4:
        print("Usage: python lc_create.py <type> <difficulty> <title>")
        sys.exit(1)

    type = sys.argv[1]
    difficulty = sys.argv[2]
    title = " ".join(sys.argv[3:])

    create_leetcode(type, difficulty, title)