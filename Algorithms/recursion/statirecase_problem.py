"""
problem link: https://www.dailycodingproblem.com/blog/staircase-problem/
"""


def staircase(n, X):
    """
    :param n: number of staircase
    :return: total number of steps
    assume only we have two move either 0-1 or 0-2 that is either one steps or two steps
    :param X: move format
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in X:
        return 1 + sum(staircase(n - x, X) for x in X if x < n)
    else:
        return sum(staircase(n - x, X) for x in X if x < n)


if __name__ == '__main__':
    total = staircase(3, [1, 2])
    print(total)
