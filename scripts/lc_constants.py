REETKODE_SOLUTION_URL = "{folder}/{filename}"
REETKODE_ICON_URL = ".github/icons/{icon}"
REETKODE_CHART_URL = ".github/lc_chart.png?"
REETKODE_FLOW_URL = ".github/lc_flow.png?"
LEETCODE_PROBLEM_URL = "https://lcid.cc/{id}"

IGNORED_DIRS = (".git", ".github", "icons", "scripts")
ACCEPTED_FILETYPES_MAP = {
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".dart": "dart",
    ".elixir": "elixir",
    ".erl": "erlang",
    ".go": "go",
    ".java": "java",
    ".js": "javascript",
    ".kt": "kotlin",
    ".php": "php",
    ".py": "python",
    ".rb": "ruby",
    ".rs": "rust",
    ".scala": "scala",
    ".sh": "shell",
    ".sql": "sql",
    ".swift": "swift",
    ".ts": "typescript",
}
LANGUAGE_ICONS_MAP = {
    "c": "c-original.svg",
    "cpp": "cplusplus-original.svg",
    "csharp": "csharp-original.svg",
    "dart": "dart-original.svg",
    "elixir": "elixir-original.svg",
    "erlang": "erlang-original.svg",
    "go": "go-original.svg",
    "java": "java-original.svg",
    "javascript": "javascript-original.svg",
    "kotlin": "kotlin-original.svg",
    "mysql": "mysql-original.svg",
    "oracle": "oracle-original.svg",
    "php": "php-original.svg",
    "pandas": "pandas-original.svg",
    "postgresql": "postgresql-original.svg",
    "python": "python-original.svg",
    "ruby": "ruby-original.svg",
    "rust": "rust-original.svg",
    "scala": "scala-original.svg",
    "shell": "bash-original.svg",
    "sql": "sql-original.svg",
    "sqlserver": "sqlserver-original.svg",
    "swift": "swift-original.svg",
    "typescript": "typescript-original.svg",
}

DATABASE_SUFFIXES = ("mysql", "sqlserver", "oracle", "pandas", "postgresql")
ROMAN_SUFFIXES = ("i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x")

LEVEL_EASY = "easy"
LEVEL_MEDIUM = "medium"
LEVEL_HARD = "hard"
LEVEL_TOTAL = "total"
DIFFICULTY_LEVELS = (LEVEL_EASY, LEVEL_MEDIUM, LEVEL_HARD)
STATS_LEVELS = (*DIFFICULTY_LEVELS, LEVEL_TOTAL)

LC_PREFIX_EASY = "lce"
LC_PREFIX_MEDIUM = "lcm"
LC_PREFIX_HARD = "lch"
LC_PREFIXES = (LC_PREFIX_EASY, LC_PREFIX_MEDIUM, LC_PREFIX_HARD)

TYPE_ALGORITHM = "algorithm"
TYPE_DATABASE = "database"
TYPE_SHELL = "shell"