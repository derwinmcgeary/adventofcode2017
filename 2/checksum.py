import csv
import math

total=0

with open('C:/Users/derwin/AOC/2/input.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
       row = list(map(int, row))
       for r in row:
           for s in row:
               if (r != s) and (max(r,s)/min(r,s) == math.floor(max(r,s)/min(r,s))):
                   print(r,s)
                   total = total + max(r,s)/min(r,s)

print(total/2)
