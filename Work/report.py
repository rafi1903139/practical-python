#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv 
import stock
import tableformat

def read_portfolio(filename):
    '''Read and returns a list of portfolio with stock price'''
    
    with open(filename, 'rt') as file:
        portdocs = parse_csv(file, 
                          select=['name', 'shares', 'price'],
                          types=[str, int, float])

    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdocs]
    return portfolio


def read_prices(filename):
    'Returns list of stocks and its prices'
    with open(filename, 'rt') as file:
        pricelist = parse_csv(file, has_headers=False, types=[str, float])
        prices = dict(pricelist)
        
    return prices


def make_report(portfolio, prices):
    rows = []

    for row in portfolio:
        holder = (row.name, row.shares, prices.get(row.name, row.price), prices.get(row.name, row.price) - row.price)

        rows.append(holder)

    return rows


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, prices, change) tuple
    '''
    headers = ['Name', 'Shares', 'Price', 'Change']
    formatter.headings(headers)
   
    #print('%10s %10s %10s %10s' %headers)
    #print(f'{'':->10s} ' * len(headers))

    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)
        #print(f'{name:>10s} {shares:>10d} {"$" + str(round(price, ndigits=2)):>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price data files
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    # Create report data
    report = make_report(portfolio=portfolio, prices=prices)
    
    # print it out
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)



def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage {argv[0]} portfile pricefile')
    
    portfile = argv[1]
    pricefile = argv[2]


    portfolio_report(portfile, pricefile)


if __name__ == '__main__':
    import sys 
    main(sys.argv)





    



