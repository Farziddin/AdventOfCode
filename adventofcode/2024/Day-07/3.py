variant = []


def set(v):
    variant.append(v)

    if len(v) > 12:
        return

    set(v + ['+'])
    set(v + ['|'])
    set(v + ['*'])


set([])
print('start')
f = open('input.txt', 'r')
summa = 0

for line in f.read().split('\n'):
    ans, v = line.split(':')
    ans = int(ans)
    values = [int(x) for x in v.split()]

    for item in variant:
        if len(item) == len(values) - 1:
            s = values[0]

            for i in range(len(item)):
                if item[i] == '|':
                    s = int(str(s) + str(values[i + 1]))
                elif item[i] == '+':
                    s += values[i + 1]
                else:
                    s *= values[i + 1]

                if s > ans:
                    break

            if s == ans:
                print(ans)
                summa += ans
                break

print(summa)
