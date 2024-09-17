# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Read a portfolio file into a list of tuples of form (name, shares, price)'''
    portfolio = []
    with open(filename, 'rt') as f:
        next(f) # header
        rows = csv.reader(f)
        for row in rows:
            portfolio.append((row[0], int(row[1]), float(row[2])))
    return portfolio

portfolio = read_portfolio('Data/portfolio.csv')

total = sum([shares * price for _, shares, price in portfolio])
print(total)
