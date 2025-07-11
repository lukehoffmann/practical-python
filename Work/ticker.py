from follow import follow
import report
import csv

columns = ['name', 'price', 'change']

def select_columns(rows, indices):
    return ([row[index] for index in indices] for row in rows)

def convert_types(rows, types):
    return ([t(val) for val, t in zip(row, types)] for row in rows)

def make_dicts(rows, keys):
    return (dict(zip(keys, row)) for row in rows)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, columns)
    return rows

def filter_symbols(rows, names):
    return (r for r in rows if r['name'] in names)

def print_stock_csv(rows):
    print(str.join(',', (h for h in columns)))
    for row in rows:
        print(str.join(',', (str(v) for v in row.values())))

def print_stock_report(rows):
    print(" ".join(["%10s" % h.title() for h in columns]))
    print(" ".join([10 * "-" for _ in columns]))
    for row in rows:
        print(str.join(' ', (str(v).rjust(10) for v in row.values())))

def ticker(portfile, logfile, format):
    portfolio = report.read_portfolio(portfile)

    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)

    if format == 'csv':
        print_stock_csv(rows)
    else:
        print_stock_report(rows)

if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'csv')
