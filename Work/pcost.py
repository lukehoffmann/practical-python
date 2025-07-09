#! /c/ProgramData/Anaconda3/python
# pcost.py
#
# Exercise 1.27

import sys
from report import read_portfolio


def main(argv):
    if len(argv) < 2:
        raise sys.exit(f"Usage: {argv[0]} filename")
    print_cost(argv[1])


def print_cost(filename):
    portfolio = read_portfolio(filename)
    cost = portfolio.total_cost
    print(f"Total cost ${cost:.2f}")


if __name__ == "__main__":
    main(sys.argv)
