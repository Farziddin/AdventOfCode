f = open('input.txt', 'r')
a = {}
nums = [int(x) for x in f.read().split()]


def check(x, step):
    global a

    if f'{x}:{step}' in a:
        return a[f'{x}:{step}']

    if step == 75:
        return 1

    l = len(str(x))
    if x == 0:
        ans = check(1, step + 1)
    elif l % 2 > 0:
        ans = check(x * 2024, step + 1)
    else:
        ans = check(int(str(x)[:l // 2]), step + 1)
        ans += check(int(str(x)[l // 2:]), step + 1)

    if x < 10:
        a[f'{x}:{step}'] = ans

    return ans


summa = 0

for x in nums:
    summa += check(x, 0)

print(summa)
