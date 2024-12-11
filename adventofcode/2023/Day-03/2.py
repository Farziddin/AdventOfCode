f = open('input.txt', 'r')
a = []
start = {}


def check(i, j):
    ans = False
    point_start = '-'
    ii = max(i - 1, 0)

    while ii < min(i + 2, len(a)):
        jj = max(j - 1, 0)

        while jj < min(j + 2, len(a)):
            if not ('0' <= a[ii][jj] <= '9' or a[ii][jj] == '.'):
                ans = True

            if a[ii][jj] == '*':
                point_start = f'{ii}, {jj}'

            jj += 1

        ii += 1

    return ans, point_start


for line in f:
    a.append([x for x in line.strip()])

for i in range(len(a)):
    s = 0
    c = False
    point_start = []

    for j in range(len(a[i]) + 1):
        if j < len(a[i]) and '0' <= a[i][j] <= '9':
            s = s * 10 + int(a[i][j])

            ans, ps = check(i, j)

            c = c or ans

            if ps not in point_start:
                point_start.append(ps)
        else:
            if s > 0 and c:
                for ps in point_start:
                    if ps == '-':
                        continue
                    if ps in start:
                        start[ps].append(s)
                    else:
                        start[ps] = [s]

            s = 0
            c = False
            point_start = []

summa = 0

for ps in start.keys():
    s = 1

    if len(start[ps]) > 1:
        for p in start[ps]:
            s *= p

        summa += s

print(summa)
