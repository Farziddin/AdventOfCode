f = open('input.txt', 'r')
a = []
summa = 0


def check(i, j):
    ii = max(i - 1, 0)

    while ii < min(i + 2, len(a)):
        jj = max(j - 1, 0)

        while jj < min(j + 2, len(a)):
            if not ('0' <= a[ii][jj] <= '9' or a[ii][jj] == '.'):
                return True

            jj += 1

        ii += 1

    return False


for line in f:
    a.append([x for x in line.strip()])

for i in range(len(a)):
    s = 0
    c = False

    for j in range(len(a[i]) + 1):
        if j < len(a[i]) and '0' <= a[i][j] <= '9':
            s = s * 10 + int(a[i][j])

            c = c or check(i, j)
        else:
            if s > 0 and c:
                summa += s

            s = 0
            c = False

print(summa)
