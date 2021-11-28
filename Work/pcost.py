# pcost.py
#
# Exercise 1.33

import report


def portfolio_cost(fn):
    """Computes the total cost (shares*price) of a portfolio file"""
    costs: float = 0
    records = report.read_portfolio(fn)
    for idx, record in enumerate(records):
        try:
            costs += record.cost
        except ValueError:
            print(f"Row {idx +1}: Bad row: {record}")
    return costs


def main(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = "Data/portfolio.csv"

    cost = portfolio_cost(filename)

    print("Total cost:", cost)


if __name__ == "__main__":
    import sys

    main(sys.argv)
