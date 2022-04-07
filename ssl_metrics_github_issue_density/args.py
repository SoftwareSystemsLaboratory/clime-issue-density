from argparse import ArgumentParser, Namespace

name: str = "CLIME"
authors: list = [
    "Nicholas M. Synovic",
    "Matthew Hyatt",
    "Sohini Thota",
    "George K. Thiruvathukal",
]


def mainArgs() -> Namespace:
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

def graphArgs() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog=f"{name} Issue Density Grapher",
        description="A tool to graph the issue density of a repository",
        epilog=f"Author(s): {', '.join(authors)}",
    )

    parser.add_argument(
        "-i",
        "--input",
        help=f"JSON export from {name} GitHub Issue Density Compute. DEFAULT: ./issue_density.json",
        type=str,
        required=False,
        default="issue_density.json",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Filename of the graph. DEFAULT: ./issue_density.pdf",
        type=str,
        required=False,
        default="issue_density.pdf",
    )
    parser.add_argument(
        "-x",
        help="Key of the x values to use for graphing. DEFAULT: defect_density",
        type=str,
        required=False,
        default="defect_density",
    )
    parser.add_argument(
        "-y",
        help="Key of the y values to use for graphing. DEFAULT: days_since_0",
        type=str,
        required=False,
        default="days_since_0",
    )
    parser.add_argument(
        "--type",
        help="Type of figure to plot. DEFAULT: line",
        type=str,
        required=False,
        default="line",
    )
    parser.add_argument(
        "--title",
        help='Title of the figure. DEFAULT: ""',
        type=str,
        required=False,
        default="",
    )
    parser.add_argument(
        "--stylesheet",
        help='Filepath of matplotlib stylesheet to use. DEFAULT: ""',
        type=str,
        required=False,
        default="",
    )

    return parser.parse_args()
