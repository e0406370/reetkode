from dataclasses import dataclass
from lc_chart import chart_leetcode
from mdutils.mdutils import MdUtils
from pygit2 import Repository
import lc_constants as lcc
import pathlib


@dataclass
class LCSolution:
    id: int
    difficulty: str
    type: str
    title: str
    folder: str
    filename: str
    icon: str


def retrieve_data() -> dict[int, list[LCSolution]]:

    lc_soln_data: dict[int, list[LCSolution]] = {}

    base_dir = pathlib.Path(__file__).parent.parent.resolve()

    for sub_dir in base_dir.iterdir():
        if sub_dir.is_file() or sub_dir.name in lcc.IGNORED_DIRS:
            continue

        for solution in sub_dir.iterdir():

            # retrieve filename
            filename = solution.name
            tokens = filename.split("_")

            # retrieve id
            id = int(tokens[1][1:])

            # retrieve difficulty
            match tokens[0]:
                case lcc.LC_PREFIX_EASY:
                    difficulty = lcc.LEVEL_EASY

                case lcc.LC_PREFIX_MEDIUM:
                    difficulty = lcc.LEVEL_MEDIUM

                case lcc.LC_PREFIX_HARD:
                    difficulty = lcc.LEVEL_HARD

            # retrieve folder
            filetype = pathlib.Path(solution).suffix
            folder = lcc.ACCEPTED_FILETYPES_MAP[filetype]

            # retrieve type
            if folder == "sql":
                type = lcc.TYPE_DATABASE

            elif folder == "shell":
                type = lcc.TYPE_SHELL

            else:
                type = lcc.TYPE_ALGORITHM

            # retrieve icon
            icon = lcc.LANGUAGE_ICONS_MAP[folder]

            # retrieve title
            title_tokens = pathlib.Path(solution).stem.split("_")[2:]
            title_tokens_len = len(title_tokens)

            if title_tokens[-1] in lcc.DATABASE_SUFFIXES:
                icon = lcc.LANGUAGE_ICONS_MAP[title_tokens[-1]]
                title_tokens.pop()
                title_tokens_len -= 1

            if title_tokens[-1] in lcc.ROMAN_SUFFIXES:
                title_tokens[-1] = title_tokens[-1].upper()
                title_tokens_len -= 1

            for i in range(title_tokens_len):
                title_tokens[i] = title_tokens[i].capitalize()

            title = f"{' '.join(title_tokens)}"

            # create LCSolution object and add to dict
            lc_soln = LCSolution(id, difficulty, type, title, folder, filename, icon)

            if id in lc_soln_data:
                lc_soln_data[id].append(lc_soln)
            else:
                lc_soln_data[id] = [lc_soln]

    # sort the dict in ascending order based on the id key
    lc_soln_data = {k: v for k, v in sorted(lc_soln_data.items(), key=lambda item: item[0])}
    return lc_soln_data


def markdown_leetcode() -> None:

    try:
        readme_file = MdUtils(file_name="README.md", title="Reetkode")
        curr_branch = Repository(".").head.shorthand
        
        readme_file.new_line(text="My personal collection of [LeetCode](https://leetcode.com/) solutions done in multiple languages, shared for learning and reference.")
        readme_file.new_line(text="This README was generated using the following custom-built **Python** scripts: [`lc_markdown.py`](scripts/lc_markdown.py), [`lc_chart.py`](scripts/lc_chart.py), and [`lc_stats.py`](scripts/lc_stats.py)")
        readme_file.new_line(text="***")
        readme_file.new_line()

        # data showing the number of LeetCode problems solved, grouped by difficulty level and programming language
        # key = programming language, value = mapping of each difficulty level to the number of problems solved
        chart_leetcode()

        # create and impose chart onto README
        chart_link_url = lcc.REETKODE_CHART_URL.format(branch=curr_branch)

        readme_file.new_line(text="## Progress Overview")
        readme_file.new_line(readme_file.new_inline_image(text="LeetCode stats", path=chart_link_url))
        readme_file.new_line()

        # data showing the list of solutions for each LeetCode problem ID with relevant metadata
        # key = problem ID, value = list of solutions corresponding to the ID
        soln_data = retrieve_data()

        # create and impose table onto README
        headers = ["ID", "Difficulty", "Type", "Title", "Solutions"]
        cells = list(headers)

        for soln_id, soln_lst in soln_data.items():
            soln_links: list[str] = []

            for soln in soln_lst:
                solution_href_url = lcc.REETKODE_SOLUTION_URL.format(
                    branch=curr_branch,
                    folder=soln.folder,
                    filename=soln.filename
                )

                icon_src_url = lcc.REETKODE_ICON_URL.format(
                    branch=curr_branch,
                    icon=soln.icon
                )

                html_anchor_img = (
                    f'<a href="{solution_href_url}">'
                    f'<img src="{icon_src_url}" height="25">'
                    f'</a>'
                )

                soln_links.append(html_anchor_img)

            soln_title = f"[{soln_lst[0].title}]({lcc.LEETCODE_PROBLEM_URL.format(id=soln_id)})"

            soln_difficulty = soln_lst[0].difficulty
            match soln_difficulty:
                case lcc.LEVEL_EASY:
                    soln_difficulty = f"🟩 {soln_difficulty.capitalize()}"

                case lcc.LEVEL_MEDIUM:
                    soln_difficulty = f"🟨 {soln_difficulty.capitalize()}"

                case lcc.LEVEL_HARD:
                    soln_difficulty = f"🟥 {soln_difficulty.capitalize()}"

            soln_type = soln_lst[0].type
            match soln_type:
                case lcc.TYPE_ALGORITHM:
                    soln_type = f"⚙️"

                case lcc.TYPE_DATABASE:
                    soln_type = f"🛢️"

                case lcc.TYPE_SHELL:
                    soln_type = f"📜"

            cells.extend(
                [
                    f"**{soln_id}**",
                    soln_difficulty,
                    soln_type,
                    soln_title,
                    " ".join(soln_links)
                ]
            )

        cols_num, rows_num = len(headers), len(soln_data)

        readme_file.new_line(text="## Solutions Directory")
        readme_file.new_table(columns=cols_num, rows=rows_num + 1, text=cells, text_align="left")
        readme_file.new_line()

        # generate README
        readme_file.create_md_file()
        print(f"[SUCCESS] README generated (table included: {rows_num} rows x {cols_num} columns)")


    except Exception as e:
        print(f"[ERROR] Failed to generate README")
        print(f"=> {e}")


if __name__ == "__main__":

    markdown_leetcode()

"""
Generates a README file summarising progress made on LeetCode:
- Displays a bar chart showing the number of solutions by programming language and difficulty level.
- Includes a table listing all solved problems with links to their respective solution files.
"""
