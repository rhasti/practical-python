# pcost.py
#
# Exercise 1.27
sum = 0
f = open('Data/portfolio.csv', 'rt')
headers = next(f).split(',')
for line in f:
    row = line.split(',')
    sum += int(row[1]) * float(row[2])

print("Total cost", sum)


f.close()