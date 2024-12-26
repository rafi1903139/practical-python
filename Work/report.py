#!/usr/bin/env python3
# report.py
#
# Exercise 2.4
from fileparse import parse_csv 
import stock

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


def print_report(report):

    headers = ('Name', 'Shares', 'Price', 'Change')
   
    print('%10s %10s %10s %10s' %headers)
    print(f'{'':->10s} ' * len(headers))

    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {"$" + str(round(price, ndigits=2)):>10s} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)


    report = make_report(portfolio=portfolio, prices=prices)
    print_report(report)



def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage {argv[0]} portfile pricefile')
    
    portfile = argv[1]
    pricefile = argv[2]


    portfolio_report(portfile, pricefile)


if __name__ == '__main__':
    import sys 
    main(sys.argv)





    



