# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Read and returns a list of portfolio with stock price'''
    
    
    portfolio = []

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row_no, row in enumerate(rows):
            record = dict(zip(headers, row))

            try:
                holding = {
                     'name': record['name'],
                     'shares': int(record['shares']),
                     'price': float(record['price'])
                }
                portfolio.append(holding)

            except ValueError: 
                    print(f"Row {row_no}: Couldn't parse the line {row}")
    
    return portfolio


def read_prices(filename):
    'Returns list of stocks and its prices'
    prices = {}
    with open(filename) as f:
          rows = csv.reader(f)

          for row in rows:
               
               if row:    
                    prices[row[0]] = float(row[1])
    return prices


def make_report(portfolio, prices):
    rows = []

    for row in portfolio:
        holder = (row['name'], row['shares'], prices.get(row['name'], row['price']), prices.get(row['name'], row['price']) - row['price'])

        rows.append(holder)

    return rows
        
portfolio_path = 'Data/portfoliodate.csv'
prices_path = 'Data/prices.csv'

portfolio = read_portfolio(portfolio_path)
prices = read_prices(prices_path)


total_cost = 0.0

for s in portfolio:
     total_cost += s['shares'] * s['price']

print('Total Cost:', total_cost)

total_value = 0.0

for s in portfolio:
     total_value += s['shares'] * prices.get(s['name'], s['price'])

print('Current value:', total_value)

gain = total_value - total_cost

print('Gain:', gain)

report = make_report(portfolio=portfolio, prices=prices)
headers = ('Name', 'Shares', 'Price', 'Change')
separator = tuple('-'*len(header) for header in headers)

print('%10s %10s %10s %10s' %headers)
print(f'{'':->10s} ' * len(headers))

for name, shares, price, change in report:
     print(f'{name:>10s} {shares:>10d} {"$" + str(round(price, ndigits=2)):>10s} {change:>10.2f}')