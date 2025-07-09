#! /c/ProgramData/Anaconda3/python
# report.py
#
# Exercise 2.4

import sys
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio


def main(argv):
    if len(argv) < 3:
        raise SystemExit(f"Usage: {argv[0]} portfolio_filename prices_filename")
    portfolio_filename = argv[1]
    prices_filename = argv[2]
    print_portfolio_report(portfolio_filename, prices_filename)


def print_portfolio_report(portfolio_filename, prices_filename):
    prices = read_prices(prices_filename)
    portfolio = read_portfolio(portfolio_filename)
    print_report(portfolio, prices)


def read_prices(filename):
    """Read a pricelist from a csv"""
    with open(filename) as f:
        prices = parse_csv(f, has_headers=False, types=[str, float])

    # Convert list  of tuples to a dictionary
    return {name: price for name, price in prices}


def read_portfolio(filename):
    '''Read a portfolio file into a list of dicts with keys "name", "shares", "price"'''
    with open(filename) as f:
        data = parse_csv(
            f, select=["name", "shares", "price"], types=[str, int, float]
        )
    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in data ]
    return Portfolio(portfolio)


def print_report(portfolio, prices):
    headers = ["Name", "Shares", "Was", "Now", "Position"]
    print(" ".join(["%10s" % header for header in headers]))
    print(" ".join([10 * "-" for _ in headers]))
    for stock in portfolio:
        old_price = stock.price
        new_price = prices[stock.name]
        value = stock.shares * new_price

        was = f"${old_price:>.2f}"
        now = f"${new_price:>.2f}"

        change = value - stock.cost
        symbol = "⬆" if change > 0.0 else "⬇" if change < 0.0 else "-"
        change_dollars = f"${abs(change):.2f}"
        print(
            f"{stock.name:>10s} {stock.shares:>10d} {was:>10s} {now:>10s} {change_dollars:>10s} {symbol}"
        )

    total = sum([value for stock in portfolio])
    print("Total value", total)


if __name__ == "__main__":
    main(sys.argv)
