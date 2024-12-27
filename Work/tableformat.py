# tableformat.py 

class Tableformatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError() 
    
    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError() 
    
class TextTableFormatter(Tableformatter):
    '''
    Emit  a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(Tableformatter):
    '''
    Output portfolio data in csv format
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(Tableformatter):
    '''
    Output portfolio in HTML format
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<td>{r}</td>', end='')
        print('</tr>')


def create_formatter(fmt):
    '''
    Returns a formatter based on the specified argument
    '''
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter() 
    elif fmt == 'html':
        return HTMLTableFormatter() 
    else:
        raise RuntimeError('Unknown format')
    

def print_table(objects, attributes, formatter):
    '''
    prints a list of object with the attributes specified
    '''
    # set the attributes as the headers
    formatter.headings(attributes)
    
    for obj in objects:
        formatter.row([str(getattr(obj, attr)) for attr in attributes])

