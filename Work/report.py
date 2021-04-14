# report.py
#
# Exercise 2.7

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


def read_prices(pr_fn):
    """read and prices as dictionary"""
    prices = {}
    with open(pr_fn, 'rt') as pr_f:
        rows = csv.reader(pr_f)
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
price_dict = read_prices('Data/prices.csv')

for position in pf:
    pf_value = position['shares'] * position["price"]
    if position["name"] in price_dict.keys():
        new_value = position['shares'] * price_dict[position["name"]]
        if pf_value < new_value:
            print(f"positive returns for {position['name']} with {position['shares']} shares is {new_value - pf_value:.2f}")
        elif pf_value > new_value:
            print(f"negative returns for {position['name']} with {position['shares']} shares is {pf_value - new_value:.2f}")
        else:
            print(f"no change in returns for  {position['name']} with {position['shares']} shares")
