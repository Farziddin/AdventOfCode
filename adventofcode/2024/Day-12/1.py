f = open('input.txt', 'r')
a = [[x for x in line.strip('\n')] for line in f.readlines()]


def check(i, j, c):
    a[i][j] = '!' + c
    ans = {
        'count': 1,
        'perimeter': 0
    }

    for x in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        if 0 <= x[0] < len(a) and 0 <= x[1] < len(a[0]) and a[x[0]][x[1]] in (c, '!' + c):
            if a[x[0]][x[1]] == c:
                d = check(x[0], x[1], c)
            else:
                d = {'count': 0, 'perimeter': 0}
        else:
            d = {'count': 0, 'perimeter': 1}

        ans['count'] += d['count']
        ans['perimeter'] += d['perimeter']

    return ans


summa = 0

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j][0] != '!':
            d = check(i, j, a[i][j])
            summa += d['count'] * d['perimeter']

print(summa)
