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
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio: list, prices: dict):
    """
    return list of tuples with stock name, shares, cost and price
    :param portfolio:
    :param prices:
    :return:

    """
    rp = []
    for stock in portfolio:
        if stock['name'] in prices.keys():
            rp.append((stock['name'], stock['shares'], prices[stock['name']], prices[stock['name']] - stock['price'] ))
    return rp


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

pf = read_portfolio('Data/portfolio.csv')
price_dict = read_prices('Data/prices.csv')

headers = ('Name', 'Shares', 'Price', 'Change')

report = make_report(pf, price_dict)

print("%10s %10s %10s %10s" % headers)
separator = '-' * 10
print(separator, separator, separator, separator)
dollar = '$'
for name, shares, price, change in report:
    dp = f"{dollar}{price:.2f}"
    print(f'{name:>10s} {shares:>10d} {dp:>10s} {change:>10.2f}')


