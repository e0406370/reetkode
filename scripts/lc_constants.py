REETKODE_BASE_URL = "https://github.com/e0406370/reetkode"
REETKODE_SOLUTION_URL = "https://github.com/e0406370/reetkode/blob/{branch}/{folder}/{filename}"

IGNORED_DIRS = (".git", "icons", "scripts")
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
    "c": "icons/c-original.svg",
    "cpp": "icons/cplusplus-original.svg",
    "csharp": "icons/csharp-original.svg",
    "dart": "icons/dart-original.svg",
    "elixir": "icons/elixir-original.svg",
    "erlang": "icons/erlang-original.svg",
    "go": "icons/go-original.svg",
    "java": "icons/java-original.svg",
    "javascript": "icons/javascript-original.svg",
    "kotlin": "icons/kotlin-original.svg",
    "mysql": "icons/mysql-original.svg",
    "oracle": "icons/oracle-original.svg",
    "php": "icons/php-original.svg",
    "postgresql": "icons/postgresql-original.svg",
    "python": "icons/python-original.svg",
    "ruby": "icons/ruby-original.svg",
    "rust": "icons/rust-original.svg",
    "scala": "icons/scala-original.svg",
    "shell": "icons/bash-original.svg",
    "sqlserver": "icons/sqlserver-original.svg",
    "swift": "icons/swift-original.svg",
    "typescript": "icons/typescript-original.svg",
}

DATABASE_SUFFIXES = ("mysql", "sqlserver", "oracle", "postgresql")
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