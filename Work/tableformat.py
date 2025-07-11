class TableFormatter:

    def headings(self, headers):
        raise NotImplementedError()


    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        print(" ".join(["%10s" % header for header in headers]))
        print(" ".join([10 * "-" for _ in headers]))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CsvTableFormatter(TableFormatter):

    def headings(self, headers):
        print(','.join(headers))


    def row(self, rowdata):
        print(','.join(rowdata))
