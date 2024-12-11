f = open('input.txt', 'r')
data = f.read().split('\n')
a = {}
summa = 0

for line in data:
    if line.count('|') > 0:
        x, y = line.split('|')
        if x in a:
            a[x].append(y)
        else:
            a[x] = [y]
    elif line.count(',') > 0:
        ords = line.split(',')
        fail = False

        for i in range(len(ords)):
            for j in range(i):
                if ords[i] in a.keys() and ords[j] in a[ords[i]]:
                    fail = True
                    break

            if fail:
                break

        if not fail:
            summa += int(ords[int(len(ords)/2)])

print(summa)
