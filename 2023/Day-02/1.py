f = open('input.txt', 'r')
colors = {
    'red': 12,
    'green': 13,
    'blue': 14
}
ans = 0

for line in f:
    game, txt = line.strip().split(':')
    tmp, game_number = game.strip().split(' ')
    fail = False

    for x in txt.strip().split(';'):
        if fail:
            break

        for y in x.strip().split(','):
            d = y.strip().split(' ')
            cnt = d[0].strip()
            color = d[1].strip()

            if color in colors and colors[color] < int(cnt):
                fail = True

                break

    if not fail:
        ans += int(game_number)

print(ans)
