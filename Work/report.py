# report.py
#
# Exercise 2.7

import fileparse
import tableformat
from stock import Stock
from portfolio import Portfolio


def read_portfolio(fn) -> Portfolio:
    """read portfolio file into portfolio data structure"""
    with open(fn, "rt") as f:
        records = fileparse.parse_csv(f, types=[str, int, float])

    portfolio = [
        Stock(record["name"], record["shares"], record["price"]) for record in records
    ]
    return Portfolio(portfolio)


def read_prices(pr_fn):
    """read and prices as dictionary"""
    with open(pr_fn, "rt") as f:
        prices_list = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    prices = {}
    for item in prices_list:
        prices[item[0]] = item[1]
    return prices


def make_report(portfolio: list, prices: dict) -> list:
    """
    return list of tuples with stock name, shares, cost and price
    :param portfolio:
    :param prices:
    :return:

    """
    rp = []
    for stock in portfolio:
        if stock.name in prices.keys():
            rp.append(
                (
                    stock.name,
                    stock.shares,
                    prices[stock.name],
                    prices[stock.name] - stock.price,
                )
            )
    return rp


def print_report(report: list, formatter) -> None:
    """
    Print formated investment report
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio: str, prices: str, fmt: str = "txt") -> None:
    """
    Top level function for report print. Ingesting portfolio and prices.
    """
    pf = read_portfolio(portfolio)
    price_dict = read_prices(prices)
    report = make_report(pf, price_dict)
    # Print it out

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv):
    if len(argv) >= 2:
        portfolio_file = argv[1]
        prices_file = argv[2]
        fmt = argv[3]
    else:
        portfolio_file = "Data/portfolio.csv"
        prices_file = "Data/prices.csv"
        fmt = "txt"

    print(f"{portfolio_file:-^43s}")
    portfolio_report(portfolio_file, prices_file, fmt)
    print()


if __name__ == "__main__":
    import sys

    main(sys.argv)
