# pcost.py
#
# Exercise 1.33

import csv
import sys


def portfolio_cost(fn):
    """Computes the total cost (shares*price) of a portfolio file"""
    costs: float = 0
    with open(fn, 'rt') as f:
        rows = csv.reader(f)
        headers=next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                costs += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return costs


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

cost = portfolio_cost(filename)
print('Total cost:', cost)
