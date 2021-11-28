# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str, select: list = None, types: list = None, has_headers: bool = True
) -> list:
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f)

        records = []

        # Read the file headers
        if has_headers:
            headers = next(rows)

            if select:
                indices: list = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
            for row in rows:
                if not row:  # Skip rows with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [row[index] for index in indices]

                if types:
                    row = [func(val) for func, val in zip(types, row)]

                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
        else:
            if types:
                for row in rows:
                    if not row:
                        continue
                    row = tuple([func(val) for func, val in zip(types, row)]) #type: ignore
                    records.append(row) #type: ignore

    return records
