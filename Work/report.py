# report.py
#
# Exercise 2.7

import fileparse


def read_portfolio(fn):
    """read portfolio file into portfolio data structure"""
    records = fileparse.parse_csv(fn, types=[str, int, float])
    return records


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
        if stock["name"] in prices.keys():
            rp.append(
                (
                    stock["name"],
                    stock["shares"],
                    prices[stock["name"]],
                    prices[stock["name"]] - stock["price"],
                )
            )
    return rp


def print_report(report: list) -> None:
    """
    Print formated investment report
    """
    headers = ("Name", "Shares", "Price", "Change")
    print("%10s %10s %10s %10s" % headers)
    separator = "-" * 10
    print((separator + " ") * len(headers))
    dollar = "$"
    for name, shares, price, change in report:
        dp = f"{dollar}{price:.2f}"
        print(f"{name:>10s} {shares:>10d} {dp:>10s} {change:>10.2f}")


def portfolio_report(portfolio: str, prices: str) -> None:
    """
    Top level function for report print. Ingesting portfolio and prices.
    """
    pf = read_portfolio(portfolio)
    price_dict = read_prices(prices)
    report = make_report(pf, price_dict)
    print_report(report)


def main(argv):
    if len(argv) >= 2:
        portfolio_file = argv[1]
        prices_file = argv[2]
    else:
        portfolio_file = "Data/portfolio.csv"
        prices_file = "Data/prices.csv"

    print(f"{portfolio_file:-^43s}")
    with open(portfolio_file, "rt") as port_file:
        with open(prices_file, "rt") as price_file:
            portfolio_report(port_file, price_file)
    print()


if __name__ == "__main__":
    import sys

    main(sys.argv)
