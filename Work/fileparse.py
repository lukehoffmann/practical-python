# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None, types=None):
    """Parse a CSV file into a list of records"""
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # Create a dictionary of selected values for each row
        records = []
        for row in rows:
            if not row:
                continue

            # Filter for the selected headers by their index in the top row
            if select:
                row = [ row[headers.index(column_name)] for column_name in select ]
            # Convert the remaining values to specified type
            if types:
                row = [ type(value) for value, type in zip(row, types) ]
            records.append(dict(zip(select or headers, row)))

        # return [make_record(row) for row in rows if row]
    return records

print(parse_csv("Data/portfolio.csv"))
print(parse_csv("Data/portfolio.csv", select=["name", "price"]))
print(parse_csv("Data/portfolio.csv", types=[str, int, float]))
