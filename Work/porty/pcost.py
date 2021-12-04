# pcost.py
#
# Exercise 1.33

# from .portfolio import Portfolio
from . import report


def portfolio_cost(fn):
    """Computes the total cost (shares*price) of a portfolio file"""
    portfolio = report.read_portfolio(fn)
    return portfolio.total_cost


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
