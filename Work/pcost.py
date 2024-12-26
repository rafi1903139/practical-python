# pcost.py
#
# Exercise 1.27
from report import read_portfolio
import sys

def portfolio_cost(filename):
    'Returns the total cost of the share of the portfolio'
    
    total_cost = 0

    portfolio = read_portfolio(filename)

    for record in portfolio:
        total_cost += record['shares'] * record['price']

    return total_cost 


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

print('Total cost', cost)