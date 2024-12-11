import re

f = open('input.txt', 'r')
summa = 0
f1 = f.read().split('\n')

for i in range(len(f1) - 1):
    if i < 1:
        continue
    for j in range(len(f1[i]) - 1):
        if j < 1:
            continue
        elif f1[i][j] == 'A':
            a = f1[i + 1][j + 1] + f1[i + 1][j - 1] + f1[i - 1][j + 1] + f1[i - 1][j - 1]

            if a.count('M') == 2 and a.count('S') == 2 and f1[i - 1][j - 1] != f1[i + 1][j + 1]:
                summa += 1

print(summa)
