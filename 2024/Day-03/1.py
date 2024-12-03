import re
f = open('input.txt', 'r')
summa = 0

for x in re.findall(r'mul\(\d+,\d+\)', f.read()):
    numbers = re.findall(r'\d+', x)
    summa += int(numbers[0]) * int(numbers[1])

print(summa)