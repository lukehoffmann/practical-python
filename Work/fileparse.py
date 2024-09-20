# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, delimeter=",", has_headers=True, select=None, types=None):
    """Parse a CSV file into a list of records"""
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimeter)

        # Read the file headers from the first row
        if has_headers:
            headers = next(rows)
        # Read the remaining rows
        records = [row for row in rows if row]

        # Select columns by their index in the top row
        if has_headers and select:
            records = [
                [record[headers.index(column_name)] for column_name in select]
                for record in records
            ]

        # Convert the remaining values to specified type
        if types:
            records = [
                [type(value) for value, type in zip(record, types)]
                for record in records
            ]

        if has_headers:
            # Create a dictionary of selected values by name
            records = [dict(zip(select or headers, record)) for record in records]
        else:
            # Create a tuple of all values
            records = [tuple(record) for record in records]

    return records


print(parse_csv("Data/portfolio.csv"))
print(parse_csv("Data/portfolio.csv", select=["name", "price"]))
print(parse_csv("Data/portfolio.csv", types=[str, int, float]))
print(parse_csv("Data/prices.csv", has_headers=False, types=[str, float]))
print(parse_csv("Data/portfolio.dat", delimeter=" ", types=[str, int, float]))
