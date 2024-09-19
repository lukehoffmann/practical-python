# report.py
#
# Exercise 2.4

from collections import Counter
import csv


def print_portfolio_report(portfolio_filename, prices_filename):
    prices = read_prices(prices_filename)
    portfolio = read_portfolio(portfolio_filename)
    print_report(portfolio, prices)


def read_prices(filename):
    """Read a pricelist from a csv"""
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        return dict([(row[0], float(row[1])) for row in reader if row])


def read_portfolio(filename):
    '''Read a portfolio file into a list of dicts with keys "name", "shares", "price"'''
    column_defs = [
        {"header": "name", "type": str},
        {"header": "shares", "type": int},
        {"header": "price", "type": float},
    ]
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        for column in column_defs:
            column["index"] = headers.index(column["header"])

        return [
            {
                column["header"]: column["type"](row[column["index"]])
                for column in column_defs
            }
            for row in rows
        ]


def print_report(portfolio, prices):
    headers = ["Name", "Shares", "Was", "Now", "Position"]
    print(" ".join(["%10s" % header for header in headers]))
    print(" ".join([10 * "-" for _ in headers]))
    for stock in portfolio:
        old_price = stock["price"]
        new_price = prices[stock["name"]]
        stock["cost"] = stock["shares"] * old_price
        stock["value"] = stock["shares"] * new_price

        was = f"${old_price:>.2f}"
        now = f"${new_price:>.2f}"

        position = stock["value"] - stock["cost"]
        symbol = ("⬆" if position > 0.0
            else "⬇" if position < 0.0
            else "-")
        position_dollars = f"${abs(position):.2f}"
        print(
            f"{stock['name']:>10s} {stock['shares']:>10d} {was:>10s} {now:>10s} {position_dollars:>10s} {symbol}"
        )

    total = sum([stock["value"] for stock in portfolio])
    print("Total value", total)


print_portfolio_report("Data/portfolio.csv", "Data/prices.csv")
