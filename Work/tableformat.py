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