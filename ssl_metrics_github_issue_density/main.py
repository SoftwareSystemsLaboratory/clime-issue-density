from argparse import Namespace
from datetime import datetime

import numpy as np
import pandas as pd
from args import getArgs
from dateutil.parser import parse
from dateutil.parser import parse as dateParse
from intervaltree import IntervalTree
from pandas import DataFrame


def getIssueTimelineIntervals(
    day0: datetime, dayN: datetime, issues: DataFrame
) -> list:
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


def buildIntervalTree(
    issues: DataFrame, commits: DataFrame, intervals: list
) -> IntervalTree:
    tree: IntervalTree = IntervalTree()

    interval: tuple
    for interval in intervals:
        tree.addi(interval[0], interval[1] + 1, 1)

    return tree


def getDailyKLOC(commits: DataFrame, timeline: list) -> list:
    dailyKLOC: list = []
    previousKLOC: float = 0

    day: int
    for day in timeline:
        klocSum: float = commits[commits["days_since_0"] == day]["kloc"].sum()

        if klocSum is np.nan:
            klocSum = previousKLOC

        dailyKLOC.append(klocSum)
        previousKLOC = klocSum

    return dailyKLOC


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
    intervalTree: IntervalTree = buildIntervalTree(issues, intervals)

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
