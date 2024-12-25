# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter = ','):
    'parse a csv file into a list of dictionary'
    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []

        if has_headers:
            headers = next(rows)
        
            if not select:
                select = headers 
            
            # get the indices of the selected column
            indices = [headers.index(colname) for colname in select]
            
            for row in rows:
                if not row: # skip row with no data
                    continue 
                
                if types:        
                    record = {name: func(row[index]) for func, name, index in zip(types, select, indices)}
                    records.append(record)
                else:
                    record = {name: row[index] for name, index in zip(select, indices)}
                    records.append(record)
        else:
            for row in rows:
                if types:
                    record = tuple(func(val) for func, val in zip(types, row))
                else:
                    record = tuple(val for val in row)

                records.append(record)

    return records 