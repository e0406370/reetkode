from lc_stats import stats_leetcode
import lc_constants as lcc
import matplotlib.pyplot as plt
import numpy as np


def chart_leetcode() -> None:

    total_stats = stats_leetcode(display=False)
    N = len(total_stats)

    languages = list(total_stats.keys())
    solutions = {
        level: np.array([stats[level] for stats in total_stats.values()])
        for level in lcc.STATS_LEVELS
    }

    fig, axes = plt.subplots()
    bottom = np.zeros(N)

    COLOR_MAP = {
        lcc.LEVEL_EASY: "mediumseagreen",
        lcc.LEVEL_MEDIUM: "gold",
        lcc.LEVEL_HARD: "lightcoral",
    }

    for level, completed in solutions.items():
        if level == lcc.LEVEL_TOTAL:
            continue

        bars = axes.bar(
            x=languages,
            height=completed,
            width=0.5,
            label=level,
            bottom=bottom,
            color=COLOR_MAP[level],
        )
        labels = [f"{int(h)}" if h > 0 else "" for h in completed]

        axes.set_autoscale_on(True)
        axes.bar_label(container=bars, labels=labels, label_type="center")

        bottom += completed

    totals = bottom
    for i, total in enumerate(totals):
        axes.annotate(
            f"{int(total)}",
            xy=(i, total),
            xytext=(0, 10),
            textcoords="offset points",
            ha="center",
            fontsize=10,
            fontweight="bold",
            color="black",
            arrowprops=dict(arrowstyle="->", color="gray", lw=2),
        )

    axes.set_ylim(0, max(totals) * 1.15)
    axes.set_title("Number of LeetCode solutions by language and level")
    axes.legend()

    chart_name = "lc_chart"
    plt.savefig(chart_name)
    print(f"[SUCCESS] Chart image '{chart_name}.png' generated (total number of solutions: {int(totals[-1])})")


if __name__ == "__main__":

    chart_leetcode()

"""
Generates a bar chart showing the number of LeetCode solutions by programming language and difficulty level, using Matplotlib and NumPy.
"""
