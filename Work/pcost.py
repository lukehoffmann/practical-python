# pcost.py
#
# Exercise 1.27

import csv

def portfolio_cost(filename):
    cost = 0.0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows) # header
        for row in rows:
            _, shares, price = row
            try:
                cost += int(shares) * float(price)
            except ValueError as e:
                print('Warning, invalid values in', row, e)
    return cost


cost = portfolio_cost('Data/portfolio.csv')
print(f"Total cost ${cost:.2f}")