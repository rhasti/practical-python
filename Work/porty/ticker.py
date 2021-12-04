# ticker.py
import csv
from .follow import follow
from .tableformat import create_formatter
from . import report


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def make_dicts(rows, headers):
    # (dict(zip(headers, row)) for row in rows)
    for row in rows:
        yield dict(zip(headers, row))


def filter_symbols(rows, names):
    for row in rows:
        if row["name"] in names:
            yield row


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ["name", "price", "change"])
    return rows


def ticker(portfolio, stock_log, fmt="txt"):
    formatter = create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    pf = report.read_portfolio(portfolio)
    rows = parse_stock_data(follow(stock_log))
    # rows = filter_symbols(rows, pf)
    rows = (row for row in rows if row["name"] in pf)
    for row in rows:
        row = [row["name"], str(row["price"]), str(row["change"])]
        formatter.row(row)


if __name__ == "__main__":
    ticker("Data/portfolio.csv", "Data/stocklog.csv", "csv")
