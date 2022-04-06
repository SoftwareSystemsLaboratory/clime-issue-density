from argparse import ArgumentParser, Namespace

name: str = "CLIME"
authors: list = ["Nicholas M. Synovic", "Matthew Hyatt", "George K. Thiruvathukal"]


def getArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{name} Issue Density",
        description="A tool to calculate the issue density of a repository",
        epilog=f"Author(s): {', '.join(authors)}",
    )

    parser.add_argument(
        "-c",
        "--commits",
        required=True,
        type=open,
        help="Commits JSON file. DEFAULT: ./commits_loc.json",
        default="commits_loc.json",
    )
    parser.add_argument(
        "-i",
        "--issues",
        required=True,
        type=open,
        help="Issues JSON file. DEFAULT: ./github_issues.json",
        default="github_issues.json",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output JSON file",
        type=str,
        required=True,
    )

    return parser.parse_args()
