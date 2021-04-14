# report.py
#
# Exercise 2.4

import sys
import csv


def read_portfolio(fn):
    """read portfolio file into portfolio data structure"""
    portfolio = []
    with open(fn, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            if len(headers) == len(row):
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
    return portfolio


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

pf = read_portfolio('Data/portfolio.csv')
print(pf)
