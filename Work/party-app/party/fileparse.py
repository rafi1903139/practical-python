# fileparse.py
#
# Exercise 3.3

import csv
import logging 

log = logging.getLogger(__name__)


def parse_csv(lines, select=None, types=None, has_headers=True, delimiter = ',', silence_errors=False):
    'parse a csv file into a list of dictionary'

    if select and not has_headers:
        raise RuntimeError('Select argument requires column headers')

    if isinstance(lines, str):
        raise RuntimeError('A list or file object is required')
    
    rows = csv.reader(lines, delimiter=delimiter)
    records = []
       

    if has_headers:
        headers = next(rows)
    
        if not select:
            select = headers 
        
        # get the indices of the selected column
        indices = [headers.index(colname) for colname in select]
        
        for row_no, row in enumerate(rows, start=1):
            

            if not row: # skip row with no data
                continue 
            
            if types:        
                try:
                    record = {name: func(row[index]) for func, name, index in zip(types, select, indices)}
                    records.append(record)

                except ValueError as v:
                    if not silence_errors:
                        print(f"Row {row_no}: Couldn't convert {row}")
                        print(f"Row {row}: Reason {v}")

            else:
                record = {name: row[index] for name, index in zip(select, indices)}
                records.append(record)
    else:
        for row in rows:
            if not row:
                continue 
            
            if types:
                try: 
                    record = tuple(func(val) for func, val in zip(types, row))

                except ValueError as v:
                    if not silence_errors:
                        log.warning("Row %d: Couldn't convert %s", row_no, row)
                        log.debug("Row %d: Reason %s", row_no, v)
                    continue
            else:
                record = tuple(val for val in row)

            records.append(record)

    return records 