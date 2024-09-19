# pcost.py
#
# Exercise 1.27

import csv
import sys


def read_portfolio(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        return [dict(zip(headers, row)) for row in rows]


def portfolio_cost(portfolio):
    for (i, item) in enumerate(portfolio):
        try:
            item['cost'] = int(item['shares']) * float(item['price'])
        except ValueError as e:
            print(f"Row {i}: Couldn't convert: {item}, {e}")

    return sum([item.get('cost', 0.0) for item in portfolio])


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


portfolio = read_portfolio(filename)
cost = portfolio_cost(portfolio)
print(f"Total cost ${cost:.2f}")