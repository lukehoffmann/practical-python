import sys
from follow import follow
import report
import tableformat
import csv

column_names = ['name', 'price', 'change']
column_indices = [0, 1, 4]
column_types = [str, float, float]

def select_columns(rows, indices):
    return ([row[index] for index in indices] for row in rows)


def convert_types(rows, types):
    return ([t(val) for val, t in zip(row, types)] for row in rows)


def make_dicts(rows, keys):
    return (dict(zip(keys, row)) for row in rows)


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, column_indices)
    rows = convert_types(rows, column_types)
    rows = make_dicts(rows, column_names)
    return rows


def filter_symbols(rows, names):
    return (r for r in rows if r['name'] in names)


def ticker(portfile, logfile, format='txt'):
    portfolio = report.read_portfolio(portfile)

    formatter = tableformat.create_formatter(format)
    formatter.headings([h.title() for h in column_names])

    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)

    for row in rows:
        formatter.row(str(v) for v in row.values())


if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise SystemExit(f"Usage: {sys.argv[0]} portfolio_filename prices_filename [csv|txt]")

    portfolio_filename = sys.argv[1]
    prices_filename = sys.argv[2]

    if len(sys.argv) > 3:
        ticker(portfolio_filename, prices_filename, sys.argv[3])
    else:
        ticker(portfolio_filename, prices_filename)
