from argparse import ArgumentParser, Namespace

name: str = "CLIME"
authors: list = [
    "Nicholas M. Synovic",
    "Matthew Hyatt",
    "Sohini Thota",
    "George K. Thiruvathukal",
]


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{name} Issue Density",
        description="A tool to calculate the issue density of a repository",
        epilog=f"Author(s): {', '.join(authors)}",
    )

    parser.add_argument(
        "-c",
        "--commits",
        type=open,
        help="Commits JSON file. DEFAULT: ./commits_loc.json",
        default="commits_loc.json",
    )
    parser.add_argument(
        "-i",
        "--issues",
        type=open,
        help="Issues JSON file. DEFAULT: ./github_issues.json",
        default="github_issues.json",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output JSON file. DEFAULT: ./issue_density.json",
        type=str,
        default="issue_density.json",
    )

    return parser.parse_args()
