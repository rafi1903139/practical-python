#!/usr/bin/env python3
# pcost.py
#
# Exercise 1.27
from report import read_portfolio
import sys

def portfolio_cost(filename):
    'Returns the total cost of the share of the portfolio'
 
    portfolio = read_portfolio(filename)

    return portfolio.total_cost

def main(argv):
    
    if len(argv) != 2:
        raise SystemExit(f'Usage {argv[0]} portfile')

    portfilename = argv[1]
    cost = portfolio_cost(portfilename)

    print('Total cost', cost)


if __name__ == '__main__':
    import sys 
    main(sys.argv)



