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
                k = 0

                while 0 <= item['x'] + dx * k < len(a) and 0 <= item['y'] + dy * k < len(a[i]):
                    st[item['x'] + dx * k, item['y'] + dy * k] = 1
                    k += 1

                k = 0
                while 0 <= i - dx * k < len(a) and 0 <= j - dy * k < len(a[i]):
                    st[i - dx * k,j - dy * k] = 1
                    k += 1

            b[a[i][j]].append({'x': i, 'y': j})

for x in a:
    print(''.join(x))

print(len(st.keys()))