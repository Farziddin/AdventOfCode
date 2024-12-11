f = open("input.txt", 'r')
summa = 0
a = []
b = []

for line in f:
    x, y = str(line).split('   ')
    a.append(int(x))
    b.append(int(y))

a.sort()
b.sort()

for i in range(len(a)):
    summa += abs(a[i] - b[i])

print(summa)
