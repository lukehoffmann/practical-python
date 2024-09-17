# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows) # header
        for (name, shares, price) in rows:
            item = dict([('name', name), ('shares', shares), ('price', price)])
            try:
                cost += int(item['shares']) * float(item['price'])
            except ValueError as e:
                print('Warning, invalid values in', item, e)
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"Total cost ${cost:.2f}")