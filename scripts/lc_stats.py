from collections import defaultdict
from tabulate import tabulate
import lc_constants as lcc
import pathlib


def stats_leetcode(display: bool = True) -> dict[str, dict[str, int]]:

    base_dir = pathlib.Path(__file__).parent.parent.resolve()
    total_stats: dict[str, dict[str, int]] = defaultdict(dict)

    for sub_dir in base_dir.iterdir():
        if sub_dir.is_file():
            continue

        language = sub_dir.name
        if language not in lcc.IGNORED_DIRS:
            stats = {
                lcc.LEVEL_EASY: 0,
                lcc.LEVEL_MEDIUM: 0,
                lcc.LEVEL_HARD: 0,
                lcc.LEVEL_TOTAL: 0,
            }

            for solution in sub_dir.iterdir():
                stats[lcc.LEVEL_TOTAL] += 1

                match solution.name[:3]:
                    case lcc.LC_PREFIX_EASY:
                        stats[lcc.LEVEL_EASY] += 1

                    case lcc.LC_PREFIX_MEDIUM:
                        stats[lcc.LEVEL_MEDIUM] += 1

                    case lcc.LC_PREFIX_HARD:
                        stats[lcc.LEVEL_HARD] += 1

            total_stats[language] = stats

    total_stats = {k: total_stats[k] for k in sorted(total_stats)}
    total_stats[lcc.LEVEL_TOTAL] = {
        level: sum(stats[level] for stats in total_stats.values())
        for level in lcc.STATS_LEVELS
    }

    if display:
        headers = [""] + [language.capitalize() for language in total_stats]
        rows = [
            [level] + [total_stats[language][level] for language in total_stats]
            for level in lcc.STATS_LEVELS
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
