# tableformat.py
from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        """
        Emit the table headings.
        """
        pass

    @abstractmethod
    def row(self, rowdata):
        """
        Emit a single row of table data.
        """
        pass


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format
    """

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format.
    """

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format.
    """

    def headings(self, headers):
        print("<tr>", end="")
        for el in headers:
            print(f"<th>{el}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for el in rowdata:
            print(f"<th>{el}</th>", end="")
        print("</tr>")


class FormatError(Exception):
    pass


def create_formatter(fmt):
    if fmt == "txt":
        formatter = TextTableFormatter()
    elif fmt == "csv":
        formatter = CSVTableFormatter()
    elif fmt == "html":
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f"Unknown table format {fmt}")
    return formatter


def print_table(report: list, cols: list, formatter: TableFormatter):
    formatter.headings(cols)
    # next(report)
    for row in report:
        rowdata = [str(getattr(row, col)) for col in cols]
        formatter.row(rowdata)
