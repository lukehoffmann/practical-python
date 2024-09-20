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
        select = select or headers
        selected_columns = {
            column_name: headers.index(column_name) for column_name in select
        }
        # Create a dictionary of selected values for each row
        make_record = lambda row: {
            column_name: row[index] for column_name, index in selected_columns.items()
        }
        return [make_record(row) for row in rows if row]


print(parse_csv("Data/portfolio.csv"))
print(parse_csv("Data/portfolio.csv", select=["name", "price"]))
