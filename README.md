# CLIME Issue Density

>

## Table of Contents

- [CLIME Issue Density](#clime-issue-density)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Licensing](#licensing)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Command Line Arguements](#command-line-arguements)

## About

The Software Systems Laboratory (SSL) GitHub Issue Density Project is a `python` tool to calculate the issue density of a GitHub repository. It is reliant upon the output of the [GitHub Issue](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-github-issues) and [Git Commits](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-git-commits-loc) tools.

### Licensing

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## How To Use

### Installation

You can install the tool via `pip` with either of the two following one-liners:

- `pip install --upgrade pip clime-metrics`
- `pip install --upgrade pip clime-issue-density`

### Command Line Arguements

`clime-issue-density-compute -h`

``` shell
options:
  -h, --help            show this help message and exit
  -c COMMITS, --commits COMMITS
                        Commits JSON file
  -i ISSUES, --issues ISSUES
                        Issues JSON file
  -o OUTPUT, --output OUTPUT
                        output JSON file
```

`clime-issue-density-graph -h`

``` shell
options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The input data file that will be read to create the graphs
  -o OUTPUT, --output OUTPUT
                        The filename to output the bus factor graph to
  -m MAXIMUM_DEGREE_POLYNOMIAL, --maximum-degree-polynomial MAXIMUM_DEGREE_POLYNOMIAL
                        Estimated maximum degree of polynomial
  -r REPOSITORY_NAME, --repository-name REPOSITORY_NAME
                        Name of the repository that is being analyzed
  --x-window-min X_WINDOW_MIN
                        The smallest x value that will be plotted
  --x-window-max X_WINDOW_MAX
                        The largest x value that will be plotted
```
