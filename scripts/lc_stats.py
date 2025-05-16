from collections import defaultdict
import pathlib

STATS_KEYS = ["easy", "medium", "hard", "total"]
EASY, MEDIUM, HARD, TOTAL = STATS_KEYS

IGNORED_DIRS = [".git", "scripts"]


def stats_leetcode() -> None:

    base_dir = pathlib.Path(__file__).parent.parent.resolve()
    total_stats: dict[str, dict[str, int]] = defaultdict(dict)

    for sub_dir in base_dir.iterdir():
        language = sub_dir.name
        if language not in IGNORED_DIRS:
            stats = {
                EASY: 0,
                MEDIUM: 0,
                HARD: 0,
                TOTAL: 0
            }

            for solution in sub_dir.iterdir():
                stats[TOTAL] += 1

                match solution.name[:3]:
                    case "lce":
                        stats[EASY] += 1
                    case "lcm":
                        stats[MEDIUM] += 1
                    case "lch":
                        stats[HARD] += 1

            total_stats[language] = stats

    total_stats[TOTAL] = {
        key: sum(stats[key] for stats in total_stats.values())
        for key in STATS_KEYS
    }

    for language, stats in total_stats.items():
        statement = (
            f"{language.capitalize()}\n"
            + "\n".join(f"{k}: {v}" for k, v in stats.items())
        )
        print(f"\n{statement}\n")


if __name__ == "__main__":
    stats_leetcode()
