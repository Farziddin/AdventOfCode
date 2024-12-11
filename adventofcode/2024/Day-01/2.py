f = open('input.txt', 'r')
summa = 0
a = []
b = []

for line in f:
    x, y = str(line).split('   ')
    a.append(int(x))
    b.append(int(y))

for x in a:
    summa += b.count(x) * x

print(summa)
