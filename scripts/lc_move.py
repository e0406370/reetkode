from lc_constants import ACCEPTED_FILETYPES
import pathlib
import shutil


def move_leetcode() -> None:

    base_dir = pathlib.Path(__file__).parent.parent.resolve()
    files_moved = 0

    for file in base_dir.iterdir():
        if file.is_dir() or file.name[:3] not in ("lce", "lcm", "lch"):
            continue

        filetype = pathlib.Path(file).suffix
        if filetype not in ACCEPTED_FILETYPES:
            print(f"[ERROR] '{file.name}' does not have an accepted filetype => {[key for key in ACCEPTED_FILETYPES.keys()]}")
            continue

        dest_dir = base_dir.joinpath(ACCEPTED_FILETYPES[filetype])

        try:
            shutil.move(src=file, dst=dest_dir / file.name)
            print(f"[SUCCESS] '{file.name}' has been moved into '{dest_dir}'")

            files_moved += 1

        except shutil.Error as e:
            print(f"[ERROR] '{file.name}' cannot be moved into '{dest_dir}'")
            print(f"=> {e}")

    print(f"[END] Total no. of files moved: {files_moved}")


if __name__ == "__main__":

    move_leetcode()

"""
Scans the base directory for LeetCode solution files and moves them into the respective language folders, based on their file extension.
"""
