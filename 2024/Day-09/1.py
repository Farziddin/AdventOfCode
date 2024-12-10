f = open("input.txt", 'r')
txt = f.read().split('\n')
a = [int(x) for x in txt[0]]
aa = []
t = 0

for i in range(len(a)):
    s = '.'
    if i % 2 == 0:
        s = str(t)
        t += 1

    for y in range(a[i]):
        aa.append(s)

y = len(aa) - 1
summa = 0
x = 0

while True:
    while x < len(aa) and aa[x] != '.':
        x += 1

    while y > 0 and aa[y] == '.':
        y -= 1

    if y <= x:
        break

    aa[x], aa[y] = aa[y], aa[x]

j = 0
for i in aa:
    if i != '.':
        summa += int(i) * j
    j += 1

print(summa)
