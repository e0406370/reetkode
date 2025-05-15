import pathlib


IGNORED = [".git", "scripts"]


def stats_leetcode() -> None:

    base_dir = pathlib.Path(__file__).parent.parent.resolve()
    for sub_dir in base_dir.iterdir():
        if sub_dir.name not in IGNORED:
            stats = {
              "easy": 0,
              "medium": 0,
              "hard": 0
            }

            for solution in sub_dir.iterdir():
                match solution.name[:3]:
                  case "lce":
                    stats["easy"] += 1
                  case "lcm":
                    stats["medium"] += 1
                  case "lch":
                    stats["hard"] += 1

            statement = (
                f"{sub_dir.name.capitalize()}\n"
                + "\n".join(f"{k}: {v}" for k, v in stats.items())
                + "\n"
                + f"total: {sum(stats.values())}"
            )
            print(f"\n{statement}\n")


if __name__ == "__main__":
    stats_leetcode()
