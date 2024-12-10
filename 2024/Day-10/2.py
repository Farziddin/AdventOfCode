f = open("input.txt", 'r')
a = [[int(x) if '0' <= x <= '9' else -1 for x in line] for line in f.read().split('\n')]


def steps(i, j):
    num = a[i][j]

    if num == 9:
        return 1

    ans = 0

    for k in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
        if 0 <= k[0] < len(a) and 0 <= k[1] < len(a[0]) and a[k[0]][k[1]] == num + 1:
            ans += steps(k[0], k[1])

    return ans


summa = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] == 0:
            summa += steps(i, j)

print(summa)
