# pcost.py
#
# Exercise 1.33

import csv
import sys


def portfolio_cost(fn):
    costs: float = 0
    with open(fn) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                costs += int(row[1]) * float(row[2])
            except ValueError:
                pass
    return costs


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

cost = portfolio_cost(filename)
print('Total cost:', cost)
