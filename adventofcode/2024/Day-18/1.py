f = open('input.txt', 'r')
mx = 70 + 1
mp = [[0 for i in range(mx)] for j in range(mx)]
lines = f.read().split('\n')
q = [[mx - 1, mx - 1, 0]]
mp[mx - 1][mx - 1] = 1
ll = 0

for i in range(1024):
    x, y = [int(m) for m in lines[i].split(',')]
    mp[x][y] = -1

for i in range(mx):
    print(''.join(['#' if x == -1 else '.' for x in mp[i]]))

while len(q):
    x, y, v = q.pop(0)
    v += 1

    if x == 0 and y == 0:
        continue

    for i, j in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
        if 0 <= i < mx and 0 <= j < mx and mp[i][j] == 0:
            mp[i][j] = v
            q.append([i, j, v])

for i in range(mx):
    print(''.join([f'{x: 4d}' for x in mp[i]]))

print(mp[0][0])
