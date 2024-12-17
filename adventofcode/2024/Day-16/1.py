f = open('input.txt', 'r')
lines = [[x for x in line] for line in f.read().splitlines()]
mp = [[0 for x in line] for line in lines]
q = []
end = []

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'E':
            end = [i, j]
        elif lines[i][j] == 'S':
            mp[i][j] = 1
            q.append([i, j, '>', 0])
        elif lines[i][j] == '#':
            mp[i][j] = -1


def walk(i, j, c, v):
    if mp[i][j] != 0 and mp[i][j] < v:
        return

    mp[i][j] = v

    if i == end[0] and j == end[1]:
        return

    x = i + (0 if c in ('<', '>') else (1 if c == 'v' else -1))
    y = j + (0 if c in ('v', '^') else (1 if c == '>' else -1))

    if x != i:
        if lines[i][j + 1] != '#':
            q.append([i, j + 1, '>', v + 1001])

        if lines[i][j - 1] != '#':
            q.append([i, j - 1, '<', v + 1001])
    else:
        if lines[i + 1][j] != '#':
            q.append([i + 1, j, 'v', v + 1001])

        if lines[i - 1][j] != '#':
            q.append([i - 1, j, '^', v + 1001])

    if lines[x][y] != '#':
        walk(x, y, c, v + 1)


while len(q) > 0:
    x = q.pop(0)

    walk(x[0], x[1], x[2], x[3])

print(mp[end[0]][end[1]])
