from follow import follow
import report
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [ t(val) for val, t in zip(row, types)]

def make_dicts(rows, keys):
    for row in rows:
        yield dict(zip(keys, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def ticker(portfile, logfile, format):
    portfolio = report.read_portfolio(portfile)
    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)
    headers = ['Name', 'Price', 'Change']
    if format == 'csv':
        print(str.join(',', (h for h in headers)))
        for row in rows:
            print(str.join(',', (str(v) for v in row.values())))
    else:
        print(" ".join(["%10s" % h for h in headers]))
        print(" ".join([10 * "-" for _ in headers]))
        for row in rows:
            print(str.join(' ', (str(v).rjust(10) for v in row.values())))

if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')
