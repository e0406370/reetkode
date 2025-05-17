from lc_stats import LEVELS, EASY, MEDIUM, HARD, TOTAL, stats_leetcode
import matplotlib.pyplot as plt
import numpy as np


def chart_leetcode() -> None:

    total_stats = stats_leetcode()
    N = len(total_stats)

    languages = list(total_stats.keys())
    solutions = {
        level: np.array([stats[level] for stats in total_stats.values()])
        for level in LEVELS
    }
    bar_width = 0.5

    fig, axes = plt.subplots()
    bottom = np.zeros(N)

    for level, completed in solutions.items():
        if level == TOTAL:
            continue
          
        color_map = {
          EASY: "mediumseagreen",
          MEDIUM: "gold",
          HARD: "lightcoral"
        }
        bars = axes.bar(
            x=languages,
            height=completed,
            width=bar_width,
            label=level,
            bottom=bottom,
            color=color_map[level],
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

    plt.savefig("lc_chart")

if __name__ == "__main__":

    chart_leetcode()
