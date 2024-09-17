# report.py
#
# Exercise 2.4

import csv
from pprint import pprint


def read_prices(filename):
    """Read a pricelist from a csv"""
    prices = {}
    with open(filename, "rt") as f:
        for row in csv.reader(f):
            if len(row) >= 1:
                prices[row[0]] = float(row[1])
    return prices


def read_portfolio(filename):
    '''Read a portfolio file into a list of dicts with keys "name", "shares", "price"'''
    portfolio = []
    with open(filename, "rt") as f:
        next(f)  # header
        for row in csv.reader(f):
            portfolio.append(
                {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            )
    return portfolio


ds = "{:.2f}"


def format_profit(change):
    symbol = ("⬆" if change > 0.0
        else "⬇" if change < 0.0
        else "-")
    return f"({symbol}{ds.format(abs(change))})"


prices = read_prices("Data/prices.csv")
pprint(prices)

portfolio = read_portfolio("Data/portfolio.csv")
pprint(portfolio)

for stock in portfolio:
    stock["old_value"] = stock["shares"] * stock["price"]
    stock["new_value"] = stock["shares"] * prices[stock["name"]]
    stock["change"] = stock["new_value"] - stock["old_value"]
    print(
        stock["name"],
        ds.format(stock["old_value"]),
        "→",
        ds.format(stock["new_value"]),
        format_profit(stock["change"]),
    )

portfolio_total = sum([stock["old_value"] for stock in portfolio])
new_total = sum([stock["new_value"] for stock in portfolio])
profit = new_total - portfolio_total
print(
    "total",
    ds.format(portfolio_total),
    "→",
    ds.format(new_total),
    format_profit(profit),
)
