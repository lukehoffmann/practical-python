# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, select=None):
    """Parse a CSV file into a list of records"""
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        # Find the index of selected headers, or use all headers
        selected_headers = {
            header: headers.index(header) for header in select or headers
        }
        # Create a dictionary of selected values for each row
        make_record = lambda row: {
            header: row[i] for header, i in selected_headers.items()
        }
        return [make_record(row) for row in rows if row]


print(parse_csv("Data/portfolio.csv"))
print(parse_csv("Data/portfolio.csv", select=["name", "price"]))
