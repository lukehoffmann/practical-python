# report.py
#
# Exercise 2.4

import csv


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


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        stock["old_value"] = stock["shares"] * stock["price"]
        stock["new_price"] = prices[stock["name"]]
        stock["new_value"] = stock["shares"] * stock["new_price"]
        stock["price_change"] = stock["new_price"] - stock["price"]
        stock["change"] = stock["new_value"] - stock["old_value"]
        report.append(
            (stock["name"], stock["shares"], stock["new_price"], stock["price_change"])
        )
    return report


prices = read_prices("Data/prices.csv")
portfolio = read_portfolio("Data/portfolio.csv")
report = make_report(portfolio, prices)

headers = ["Name", "Shares", "Price", "Change"]
print(" ".join(["%10s" % header for header in headers]))
print(" ".join([10 * "-" for _ in headers]))
for name, shares, price, change in report:
    price = f"${price:>.2f}"
    symbol = ("⬆" if change > 0.0
         else "⬇" if change < 0.0
         else "-")
    change = f"{symbol} ${abs(change):.2f}"
    print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10s}")
