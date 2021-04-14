# report.py
#
# Exercise 2.6

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
                holding = {
                    'name': row[0],
                    'shares': int(row[1]),
                    'price': float(row[2])
                }
                portfolio.append(holding)
    return portfolio


def read_prices(pfn):
    """read and prices as dictionary"""
    prices = {}
    with open(pfn, 'rt') as pf:
        rows = csv.reader(pf)
        headers = next(rows)
        for row in rows:
            if len(headers) == len(row):
                prices[row[0]] = float(row[1])
    return prices


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

pf = read_portfolio('Data/portfolio.csv')
print(pf)
