from dataclasses import dataclass
from lc_stats import stats_leetcode
from mdutils.mdutils import MdUtils
from pygit2 import Repository
import lc_constants as lcc
import pathlib


@dataclass
class LCSolution:
    id: int
    difficulty: str
    title: str
    folder: str
    filename: str
    icon: str


def retrieve_data() ->  dict[int, list[LCSolution]]:

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
            lc_soln = LCSolution(id, difficulty, title, folder, filename, icon)

            if id in lc_soln_data:
                lc_soln_data[id].append(lc_soln)
            else:
                lc_soln_data[id] = [lc_soln]

    # sort the dict in ascending order based on the id key
    lc_soln_data = {k: v for k, v in sorted(lc_soln_data.items(), key=lambda item: item[0])}
    return lc_soln_data


def markdown_leetcode() -> None:

    readme_file = MdUtils(file_name="README.md", title="Reetkode")
    curr_branch = Repository(".").head.shorthand
    
    # data showing the list of solutions for each LeetCode problem ID with relevant metadata
    # key = problem ID, value = list of solutions corresponding to the ID
    soln_data = retrieve_data()
    
    # data showing the number of LeetCode problems solved, grouped by difficulty level and programming language
    # key = programming language, value = mapping of each difficulty level to the number of problems solved
    stats_data = stats_leetcode(display=False)

    # soln_data => create the table
    headers = ["ID", "Difficulty", "Title", "Solutions"]
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

        soln_title = soln_lst[0].title

        soln_difficulty = soln_lst[0].difficulty
        match soln_difficulty:
            case lcc.LEVEL_EASY:
                soln_difficulty = f"🟩 {soln_difficulty.capitalize()}"

            case lcc.LEVEL_MEDIUM:
                soln_difficulty = f"🟨 {soln_difficulty.capitalize()}"

            case lcc.LEVEL_HARD:
                soln_difficulty = f"🟥 {soln_difficulty.capitalize()}"
        
        cells.extend(
            [
                f"**{soln_id}**",
                soln_difficulty,
                soln_title,
                " ".join(soln_links)
            ]
        )

    readme_file.new_line()
    readme_file.new_table(columns=len(headers), rows=len(soln_data) + 1, text=cells, text_align="left")

    readme_file.create_md_file()


if __name__ == "__main__":

    markdown_leetcode()