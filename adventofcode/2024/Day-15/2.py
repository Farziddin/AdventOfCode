f = open('input.txt', 'r')
mp = []
move_key = {}
is_map = True
i = 0
j = 0


def add_move(i, j, x):
    if x not in move_key.keys():
        move_key[x] = []

    if [i, j] not in move_key[x]:
        move_key[x].append([i, j])


def check_movie(i, j, x, s):
    add_move(i, j, s)

    if x in ('>', '<'):
        m = 1 if x == '>' else -1

        if mp[i][j + m] == '.':
            return True
        elif mp[i][j + m] == '#':
            return False
        else:
            if check_movie(i, j + m, x, s + 1):
                add_move(i, j, s)

                return True
            else:
                return False
    else:
        m = 1 if x == 'v' else -1

        if mp[i + m][j] == '.':
            return True
        elif mp[i + m][j] == '#':
            return False
        else:
            if check_movie(i + m, j, x, s + 1) and check_movie(i + m, j + (1 if mp[i + m][j] == '[' else -1), x, s + 1):
                return True
            else:
                return False


def moves(k):
    keys = sorted(move_key.keys(), reverse=True)

    a = 1 if k in 'v' else (-1 if k == '^' else 0)
    b = 1 if k in '>' else (-1 if k == '<' else 0)

    for l in keys:
        for x in move_key[l]:
            mp[x[0]][x[1]], mp[x[0] + a][x[1] + b] = mp[x[0] + a][x[1] + b], mp[x[0]][x[1]]


ii = 0

for line in f.read().splitlines():
    if len(line) == 0:
        is_map = False

        continue

    if is_map:
        mp.append([])

        for x in range(len(line)):
            if line[x] == '@':
                i = ii
                j = len(mp[-1])

            if line[x] == 'O':
                mp[-1].append('[')
                mp[-1].append(']')
            elif line[x] == '#':
                mp[-1].append('#')
                mp[-1].append('#')
            else:
                mp[-1].append('.')
                mp[-1].append('.')

        ii += 1
    else:
        for x in line:
            if x in ('^', '>', '<', 'v'):
                move_key = {}
                if check_movie(i, j, x, 1):
                    moves(x)

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
        if mp[i][j] == '[':
            summa += i * 100 + j

print(summa)
