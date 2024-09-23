# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, delimeter=',', has_headers=True, select=None, types=None, silence_errors=False):
    """Parse a CSV file into a list of records"""
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimeter)

        if select and not has_headers and not silence_errors:
            raise RuntimeError("select argument requires column headers")

        # Read the file headers from the first row
        if has_headers:
            headers = next(rows)

        records = []
        for row in rows:
            if not row:
                continue

            # Select columns by their index in the top row
            if has_headers and select:
                row = [ row[headers.index(column_name)] for column_name in select ]

            # Convert the remaining values to specified type
            if types:
                row = [ type(value) for value, type in zip(row, types) ]

            if has_headers:
                # Create a dictionary of selected values by name
                records.append(dict(zip(select or headers, row)))
            else:
                # Create a tuple of all values
                records.append(tuple(row))

    return records

# print(parse_csv("Data/portfolio.csv"))
# print(parse_csv("Data/portfolio.csv", select=["name", "price"]))
# print(parse_csv("Data/portfolio.csv", types=[str, int, float]))
# print(parse_csv("Data/prices.csv", has_headers=False, types=[str, float]))
# print(parse_csv("Data/portfolio.dat", delimeter=' ', types=[str, int, float]))
# print(parse_csv("Data/portfolio.csv", select=["name", "shares"], has_headers=False, silence_errors=True))
