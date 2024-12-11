f = open('input.txt', 'r')
lines = f.read().split('\n')
a = [[x for x in line] for line in lines]
summa = 0
b = {}
st = {}

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] not in ('.', '#'):
            if a[i][j] not in b:
                b[a[i][j]] = []

            for item in b[a[i][j]]:
                dx = item['x'] - i
                dy = item['y'] - j

                if 0 <= item['x'] + dx < len(a) and 0 <= item['y'] + dy < len(a[i]):
                    # a[item['x'] + dx][item['y'] + dy] = '#'
                    summa += 1
                    st[item['x'] + dx, item['y'] + dy] = 1

                if 0 <= i - dx < len(a) and 0 <= j - dy < len(a[i]):
                    # a[i - dx][j - dy] = '#'
                    summa += 1
                    st[i - dx,j - dy] = 1

            b[a[i][j]].append({'x': i, 'y': j})

for x in a:
    print(''.join(x))

print(len(st.keys()))