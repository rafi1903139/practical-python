# pcost.py
#
# Exercise 1.27
import csv 
import sys 

def portfolio_cost(filename):
    'Returns the total cost of the share of the portfolio'
    f = open(filename,'rt')
    rows = csv.reader(f)
    
    # points the rows after header
    headers = next(rows)
    
    total_cost = 0


    for row_no, row in enumerate(rows,start=1):
        record = dict(zip(headers, row))

        try:
            shares, price = int(record['shares']), float(record['price'])
            total_cost += (shares * price)

        except ValueError:
            print(f"Row {row_no}: Couldn't convert: {row}")

    return total_cost 


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)

print('Total cost', cost)