# pcost.py
#
# Exercise 1.32

import csv

def portfolio_cost(filename):
    costs: float = 0
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                costs += int(row[1]) * float(row[2])
            except ValueError:
                pass
    return costs


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)


