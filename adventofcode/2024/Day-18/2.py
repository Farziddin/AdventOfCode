f = open('input.txt', 'r')
mx = 70 + 1
blocks = []

for line in f.read().split('\n'):
    x, y = [int(m) for m in line.split(',')]
    blocks.append([x, y])
    mp = [[0 for i in range(mx)] for j in range(mx)]
    q = [[mx - 1, mx - 1, 0]]
    mp[mx - 1][mx - 1] = 1

    for x, y in blocks:
        mp[x][y] = -1

    while len(q):
        x, y, v = q.pop(0)
        v += 1

        if x == 0 and y == 0:
            continue

        for i, j in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
            if 0 <= i < mx and 0 <= j < mx and mp[i][j] == 0:
                mp[i][j] = v
                q.append([i, j, v])

    if mp[0][0] == 0:
        print(line)
        break
