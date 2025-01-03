# ticker.py

from follow import follow 
from report import read_portfolio
from tableformat import create_formatter, print_table
import csv 

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dict(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def filter_symbols(rows, names):
    return (row for row in rows if row['name'] in names)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dict(rows, ['name', 'price', 'change'])

    return rows 

def ticker(portfile, logfile, fmt='txt'):
    
    portfolio = read_portfolio(portfile)
    formatter = create_formatter(fmt) 

    rows = parse_stock_data(follow(logfile))
    rows = filter_symbols(rows, portfolio)

    headers = ['name', 'price', 'change']

    formatter.headings(headers)

    for row in rows:
        formatter.row(list(map(str, row.values())))
        

def main(argv):
    
    ticker(argv[1], argv[2], argv[3])


if __name__ == '__main__':
    import sys 

    if len(sys.argv) != 4:
        raise UserWarning('Usage portfile logfile')
    
    main(sys.argv)