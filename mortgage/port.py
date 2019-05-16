# port.py
import csv
total = 0.0
with open('Book.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)   # Skip a single input
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        total = row[2]*row[3]

print(total)