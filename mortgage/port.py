# port.py
import csv
# Don't catch all errors by using except exception
# print statements 

def read_portfolio(filename, *, errors='warn'):
    """
    Read a csv file when name, date, shares, price data into a list
    """
    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("Error must be one of 'warn', 'silent', 'raise'")
    portfolio= []
    with open('Book.csv', 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip a single input
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == warn:
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Reason:', err)
                elif errors == 'raise':  # Reraises the last exception
                    raise
                else:
                    pass # Ignore
                continue  # Skipts to the next line
            # record = tuple(row)
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
            }
            portfolio.append(record)
    return  portfolio

portfolio = read_portfolio('Book.csv')
print(portfolio)

total = 0.0

for holding in portfolio:
    total += holding['shares'] * holding['price']   #shares * price
print('Total Cost: ', total)
# total = portfolio_cost('Book.csv', errors='warn')
# print('Total Cost: ', total)