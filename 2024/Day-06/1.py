import copy

f = open("input.txt", 'r')
mp = []
for line in f.read().split('\n'):
    mp.append([x for x in line])


i = 0
j = -1
rl = ['u', 'r', 'd', 'l']
for line in mp:
    t = 0
    for x in line:
        if mp[i][t] == '^':
            mp[i][t] = 'u'
            j = t
            break
        t += 1
    if j >= 0:
        break
    i += 1

def check(m, i, j, x, y):
    m[x][y] = '#'
    r = 'u'
    step = 0
    while True:
        step += 1
        if r == 'u' and i == 0 or r == 'd' and i == len(m) - 1 or r == 'r' and j == len(m[0]) - 1 or r == 'l' and j == 0:
            break
        elif step > 10000:
            return 1
        elif r == 'u' and m[i - 1][j] != '#':
            i -= 1
        elif r == 'd' and m[i + 1][j] != '#':
            i += 1
        elif r == 'r' and m[i][j + 1] != '#':
            j += 1
        elif r == 'l' and m[i][j - 1] != '#':
            j -= 1
        else:
            if r == 'u':
                r = 'r'
            elif r == 'r':
                r = 'd'
            elif r == 'd':
                r = 'l'
            elif  r == 'l':
                r = 'u'
        m[i][j] = r

    return 0
summa = 0
mn = mp.copy()
for x in range(len(mp)):
    for y in range(len(mp[i])):
        if mp[x][y] == '.':
            mp = mn.copy()
            summa += check(copy.deepcopy(mp), i, j, x, y)


print(summa)