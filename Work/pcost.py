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
    cost = portfolio_cost(portfolio)
    print(f"Total cost ${cost:.2f}")


def portfolio_cost(portfolio):
    for (i, item) in enumerate(portfolio):
        try:
            item['cost'] = int(item['shares']) * float(item['price'])
        except ValueError as e:
            print(f"Row {i}: Couldn't convert: {item}, {e}")

    return sum([item.get('cost', 0.0) for item in portfolio])


if __name__ == "__main__":
    main(sys.argv)
