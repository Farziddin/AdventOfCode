f = open('input.txt', 'r')
mp = []
is_map = True
i = 0
j = 0


def moves(i, j, x):
    global mp

    a, b = 0, 0
    if x == '^':
        a = -1
    elif x == '>':
        b = 1
    elif x == '<':
        b = -1
    elif x == 'v':
        a = 1

    if mp[i + a][j + b] == '.':
        mp[i + a][j + b], mp[i][j] = mp[i][j], mp[i + a][j + b]

        return True
    elif mp[i + a][j + b] == 'O':
        if moves(i + a, j + b, x):
            mp[i + a][j + b], mp[i][j] = mp[i][j], mp[i + a][j + b]

            return True

    return False


for line in f.read().splitlines():
    if len(line) == 0:
        is_map = False
        continue

    if is_map:
        mp.append([x for x in line])

        for x in range(len(line)):
            if line[x] == '@':
                i = len(mp) - 1
                j = x
                mp[i][j] = '.'

    else:
        for x in line:
            if x in ('^', '>', '<', 'v') and moves(i, j, x):
                if x == '^':
                    i -= 1
                elif x == '>':
                    j += 1
                elif x == 'v':
                    i += 1
                elif x == '<':
                    j -= 1

summa = 0

for i in range(len(mp)):
    for j in range(len(mp[0])):
        if mp[i][j] == 'O':
            summa += i * 100 + j

print(summa)
