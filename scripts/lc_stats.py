from collections import defaultdict
from lc_constants import IGNORED_DIRS, STATS_LEVELS, EASY, MEDIUM, HARD, TOTAL
from tabulate import tabulate
import pathlib


def stats_leetcode(display: bool = True) -> dict[str, dict[str, int]]:

    base_dir = pathlib.Path(__file__).parent.parent.resolve()
    total_stats: dict[str, dict[str, int]] = defaultdict(dict)

    for sub_dir in base_dir.iterdir():
        if sub_dir.is_file():
            continue

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
        level: sum(stats[level] for stats in total_stats.values())
        for level in STATS_LEVELS
    }

    if display:
        headers = [""] + [language.capitalize() for language in total_stats]
        rows = [
            [level] + [total_stats[language][level] for language in total_stats]
            for level in STATS_LEVELS
        ]
        print(tabulate(tabular_data=rows, headers=headers, tablefmt="grid"))

    return dict(total_stats)


if __name__ == "__main__":

    stats_leetcode()

"""
Displays a formatted summary table in the CLI showing the number of LeetCode problems solved, grouped by difficulty level and programming language.

+--------+--------+--------------+----------+-------+---------+
|        |   Java |   Javascript |   Python |   Sql |   Total |
+========+========+==============+==========+=======+=========+
| easy   |      0 |            0 |        0 |     0 |       0 |
+--------+--------+--------------+----------+-------+---------+
| medium |      0 |            0 |        0 |     0 |       0 |
+--------+--------+--------------+----------+-------+---------+
| hard   |      0 |            0 |        0 |     0 |       0 |
+--------+--------+--------------+----------+-------+---------+
| total  |      0 |            0 |        0 |     0 |       0 |
+--------+--------+--------------+----------+-------+---------+
"""
