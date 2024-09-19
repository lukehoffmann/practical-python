# report.py
#
# Exercise 2.4

from collections import Counter
import csv


def read_prices(filename):
    """Read a pricelist from a csv"""
    with open(filename, "rt") as f:
        reader = csv.reader(f)
        return dict(
            [(row[0], float(row[1])) for row in reader if row]
        )


def read_portfolio(filename):
    '''Read a portfolio file into a list of dicts with keys "name", "shares", "price"'''
    required_columns = ["name", "shares", "price"]
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        column_indices = { column: headers.index(column) for column in required_columns }
        portfolio = [ { column: row[i] for column, i in column_indices.items() } for row in rows]

    for stock in portfolio:
        stock['shares'] = int(stock['shares'])
        stock['price'] = float(stock['price'])
    return portfolio


prices = read_prices("Data/prices.csv")
portfolio = read_portfolio("Data/portfolio.csv")

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
    print(f"{stock['name']:>10s} {stock['shares']:>10d} {was:>10s} {now:>10s} {position_dollars:>10s} {symbol}")

total = sum([stock["value"] for stock in portfolio])
print ('Total value', total)
