#! /c/ProgramData/Anaconda3/python
# report.py
#
# Exercise 2.4

import sys
from fileparse import parse_csv
from stock import Stock
from portfolio import Portfolio
import tableformat

def portfolio_report(portfolio_filename, prices_filename, format="txt"):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    data = report_data(portfolio, prices)

    formatter = tableformat.create_formatter(format)
    print_report(data, formatter)

    print("Total value", portfolio.total_value(prices))


def read_prices(filename):
    """Read a pricelist from a csv"""
    with open(filename) as f:
        prices = parse_csv(f, has_headers=False, types=[str, float])

    return dict(prices)


def read_portfolio(filename):
    '''Read a portfolio file into a list of dicts with keys "name", "shares", "price"'''
    with open(filename) as f:
        data = parse_csv(
            f, select=["name", "shares", "price"], types=[str, int, float]
        )
    portfolio = [ Stock(d['name'], d['shares'], d['price']) for d in data ]
    return Portfolio(portfolio)


def report_data(portfolio, prices):
    for stock in portfolio:
        old_price = stock.price
        new_price = prices[stock.name]

        change = new_price - old_price
        position = stock.value(new_price) - stock.cost
        symbol = "📈" if position > 0.0 else "📉" if position < 0.0 else ""

        yield (stock.name, stock.shares, old_price, new_price, change, position, symbol)


def print_report(reportdata, formatter):
    formatter.headings(["Name", "Shares", "Was", "Now", "Change", "Position"])
    for name, shares, was, now, change, position, symbol in reportdata:
        formatter.row([name, str(shares), f'${was:>.2f}', f'${now:>.2f}', f'{change:>.2f}{symbol}', f'{position:>.2f}'])


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(f"Usage: {sys.argv[0]} portfolio_filename prices_filename [csv|text]")

    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]

    if len(sys.argv) > 3:
        portfolio_report(portfolio_filename, prices_filename, sys.argv[3])
    else:
        portfolio_report(portfolio_filename, prices_filename)
