from argparse import Namespace
from datetime import datetime

import numpy as np
import pandas as pd
from dateutil.parser import parse
from intervaltree import IntervalTree
from pandas import DataFrame
from dateutil.parser import parse as dateParse
from args import getArgs


def getIssueTimelineIntervals(day0: datetime, dayN: datetime, issues: DataFrame)    -> list:
    intervals = []

    foo: str
    bar: str
    for foo, bar in zip(issues["created_at"], issues["closed_at"]):
        try:
            startDate: datetime = dateParse(foo)
        except TypeError:
            startDate: datetime = foo

        try:
            endDate: datetime = dateParse(bar)
        except TypeError:
            endDate: datetime = bar

        startDate.replace(tzinfo=None)
        endDate.replace(tzinfo=None)

        startDaySince0 = (startDate.replace(tzinfo=None) - day0).days
        endDaySince0 = (endDate.replace(tzinfo=None) - day0).days

        intervals.append((startDaySince0, endDaySince0))

    return intervals


# def build_tree(*, issues, commits, intervals) -> IntervalTree:
#     """builds interval tree

#     :param commits: DataFrame
#     :param issues: DataFrame
#     :param intervals: list

#     :return tree: IntervalTree
#     """

#     tree = IntervalTree()

#     # add all items to interval tree
#     for interval in intervals:
#         tree.addi(interval[0], interval[1] + 1, 1)

#     return tree


# def get_daily_kloc(commits):
#     """returns a list of average kloc per day"""

#     first, last, days = get_timestamp()

#     daily_kloc = []
#     prev = 0
#     for day in days:
#         avg_kloc = commits[commits["days_since_0"] == day]["kloc"].mean()
#         daily_kloc.append(avg_kloc if not avg_kloc is np.nan else prev)
#         prev = avg_kloc if not avg_kloc is np.nan else prev

#     return daily_kloc


# def get_daily_defects(tree):
#     """returns a list of number of defects per day"""

#     first, last, days = get_timestamp()

#     defects = []
#     for day in days:
#         defects.append(len(tree[day]))

#     return defects


def main():
    args: Namespace = getArgs()

    commits: DataFrame = pd.read_json(args.commits)
    issues: DataFrame = pd.read_json(args.issues).T

    day0: datetime = dateParse(issues["created_at"][0]).replace(tzinfo=None)
    dayN: datetime = datetime.now().replace(tzinfo=None)
    timeline: list = [day for day in range((dayN - day0).days)]

    issues["created_at"] = issues["created_at"].fillna(day0)
    issues["closed_at"] = issues["closed_at"].fillna(dayN)

    intervals: list = getIssueTimelineIntervals(day0, dayN, issues)
    # tree = build_tree(issues=issues, commits=commits, intervals=intervals)

    # first, last, days = get_timestamp()

    # kloc = get_daily_kloc(commits)
    # defects = get_daily_defects(tree)
    # ddensity = [nd / k for nd, k in zip(defects, kloc)]

    # d = {
    #     "days_since_0": days,
    #     "defect_density": ddensity,
    # }

    # out = pd.DataFrame(data=d)
    # out.to_json(args.output)


if __name__ == "__main__":
    main()
