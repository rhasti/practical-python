# report.py
#
# Exercise 2.7

import fileparse
import tableformat
from stock import Stock


def read_portfolio(fn):
    """read portfolio file into portfolio data structure"""
    records = fileparse.parse_csv(fn, types=[str, int, float])
    stock_list = []
    for record in records:
        stock = Stock(record["name"], record["shares"], record["price"])
        stock_list.append(stock)
    return stock_list


def read_prices(pr_fn):
    """read and prices as dictionary"""
    prices_list = fileparse.parse_csv(pr_fn, types=[str, float], has_headers=False)
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
    with open(portfolio, "rt") as f:
        pf = read_portfolio(f)
    with open(prices, "rt") as f:
        price_dict = read_prices(f)
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

    print(f"{portfolio_file:-^43s}")
    portfolio_report(portfolio_file, prices_file, fmt)
    print()


if __name__ == "__main__":
    import sys

    main(sys.argv)
