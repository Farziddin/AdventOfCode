f = open("input.txt", 'r')
txt = f.read().split('\n')
a = [int(x) for x in txt[0]]
aa = []
t = 0
dd = []

for i in range(len(a)):
    s = '.'
    if i % 2 == 0:
        s = str(t)
        t += 1

    if a[i] > 0:
        dd.append([s for x in range(a[i])])

ans = []

for i in range(len(dd)):
    if len(dd[i]) == 0:
        continue
    if dd[i][0] != '.':
        ans.append(dd[i])
    else:
        j = len(dd) - 1
        il = len(dd[i])

        while j > i:
            jl = len(dd[j])
            if 0 < jl <= il and dd[j][0] != '.':
                ans.append(dd[j])
                il -= jl
                dd[j] = ['.' for _ in range(jl)]

                if il == 0:
                    break

            j -= 1

        if il > 0:
            ans.append(['.' for _ in range(il)])

summa = 0
j = 0
print(ans)
line = []
for d in ans:
    for x in d:
        line.append(x)
        if x != '.':
            summa += int(x) * j
        j += 1
print(line)
print(summa)
