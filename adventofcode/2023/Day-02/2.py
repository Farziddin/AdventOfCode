f = open('input.txt', 'r')
ans = 0

for line in f:
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    game, txt = line.strip().split(':')

    for x in txt.strip().split(';'):
        for y in x.strip().split(','):
            d = y.strip().split(' ')
            cnt = d[0].strip()
            color = d[1].strip()

            if color in colors and colors[color] < int(cnt):
                colors[color] = int(cnt)

    ans += colors['red'] * colors['green'] * colors['blue']

print(ans)
