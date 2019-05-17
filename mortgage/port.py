# port.py
import csv

def portfolio_cost(filename):
    total = 0.0
    with open('Book.csv', 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)   # Skip a single input
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                print('Row:', rowno, 'Bad row:', row)
                print('Row:', rowno, 'Reason:', err)
                continue    # Skips to the next row
            total += row[2]*row[3]

    return total

total = portfolio_cost('Book.csv')
print('Total Cost: ', total)