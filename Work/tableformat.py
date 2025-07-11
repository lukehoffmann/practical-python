class TableFormatter:

    def headings(self, headers):
        raise NotImplementedError()


    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        print(" ".join("%10s" % header for header in headers))
        print(" ".join(10 * "-" for _ in headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CsvTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers))


    def row(self, rowdata):
        print(','.join(rowdata))


def create_formatter(format):
    if format == 'csv':
        return CsvTableFormatter()
    elif format == 'txt':
        return TextTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {format}')


def print_table(data, attrs, formatter):
    formatter.headings([a.title() for a in attrs])
    for d in data:
        formatter.row([str(getattr(d, a)) for a in attrs])
