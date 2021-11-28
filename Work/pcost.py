# pcost.py
#
# Exercise 1.33

import csv
import sys
import report


def portfolio_cost(fn):
    """Computes the total cost (shares*price) of a portfolio file"""
    costs: float = 0
    records = report.read_portfolio(fn)
    for idx, record in enumerate(records):
        try:
            nshares = int(record["shares"])
            price = float(record["price"])
            costs += nshares * price
        except ValueError:
            print(f"Row {idx +1}: Bad row: {record}")
    return costs


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)

cost = portfolio_cost(filename)
print("Total cost:", cost)
