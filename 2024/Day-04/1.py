import re

f = open('input.txt', 'r')
summa = 0
f1 = []
f2 = []
f3 = []
f4 = []

for line in f:
    f1.append(line)
    i = 0
    for x in line:
        if len(f2) < i + 1:
            f2.append(x)
        else:
            f2[i] += x

        i += 1
for i in range(len(f1[0])):
    dd = ''
    d = ''
    k = 0
    for j in range(len(f2) - i):
        try:
            dd += f1[j + i][j]
        except:
            pass

        try:
            d += f1[j][j + i]
        except:
            pass
        k += 1

    f3.append(dd)
    f3.append(d)

for i in range(len(f1[0])):
    dd = ''
    d = ''
    k = 0
    for j in range(len(f2) - i):
        try:
            dd += f1[j + i][len(f2) - j]
        except:
            pass

        try:
            d += f1[j][len(f2) - (j + i)]
        except:
            pass
        k += 1

    f4.append(dd)
    f4.append(d)

for x in [f1, f2, f3, f4]:
    for line in x:
        summa += len(re.findall(r'XMAS', line)) + len(re.findall(r'SAMX', line))
print(summa)
