import fileparse
import gzip

with open('Data/portfolio.csv') as f:
    port = fileparse.parse_csv(f, types=[str, int, float])
    print(port)

with gzip.open('Data/portfolio.csv.gz', 'rt') as file:
    port = fileparse.parse_csv(file, types=[str, int, float])
    print(port)

lines = ['name,shares,price', 'AA,100,34.23', 'IBM,50,91.1', 'HPE,75,45.1']
port = fileparse.parse_csv(lines, types=[str,int,float])
print(port)

port = fileparse.parse_csv('Data/portfolio.csv', types=[str,int,float])
print(port)
