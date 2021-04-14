# pcost.py
#
# Exercise 1.30

def portfolio_cost(filename):
    costs: float = 0
    with open(filename, 'rt') as f:
        headers = next(f).split(',')
        for line in f:
            row = line.split(',')
            costs += int(row[1]) * float(row[2])
    return costs


cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)
