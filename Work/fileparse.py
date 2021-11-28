# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(
    filename: str,
    select: list = None,
    types: list = None,
    has_headers: bool = True,
    delimiter=",",
    silence_errors=False,
) -> list:
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        records = []

        # Read the file headers
        if has_headers:
            headers = next(rows)

            if select:
                indices: list = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
            for idx, row in enumerate(rows):
                idx += 1
                if not row:  # Skip rows with no data
                    continue
                # Filter the row if specific columns were selected
                if indices:
                    row = [row[index] for index in indices]

                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        if not silence_errors:
                            print(f"Row {idx}: Couldn't convert {row}")
                            print(f"Row {idx}: Reason {e}")

                # Make a dictionary
                record = dict(zip(headers, row))
                records.append(record)
        else:
            if select:
                raise RuntimeError("select argument requires column headers")
            if types:
                for idx, row in enumerate(rows):
                    idx += 1
                    if not row:
                        continue
                    try:
                        row = tuple([func(val) for func, val in zip(types, row)])  # type: ignore
                    except ValueError as e:
                        if not silence_errors:
                            print(f"Row {idx}: Couldn't convert {row}")
                            print(f"Row {idx}: Reason {e}")

                    records.append(row)  # type: ignore

    return records
