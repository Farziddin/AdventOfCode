import re

f = open('input.txt', 'r')
txt = f.read()
summa = 0
a = {
    0: 1
}

for x in re.finditer(r'do\(\)', txt):
    a[x.span()[0]] = 1
for x in re.finditer(r"don't\(\)", txt):
    a[x.span()[0]] = 0

keys = a.keys()
keys = sorted(keys)

for x in re.finditer(r'mul\(\d+,\d+\)', txt):
    start = x.span()[0]
    j = 0
    while True:
        if j + 1 >= len(keys) or keys[j + 1] > start:
            break
        j += 1

    numbers = re.findall(r'\d+', x.group())
    summa += a[keys[j]] * int(numbers[0]) * int(numbers[1])

print(summa)
