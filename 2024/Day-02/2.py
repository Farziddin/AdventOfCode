f = open("input.txt", 'r')


def check(numbers):
    old = None
    dif = None
    for x in numbers:
        if old:
            if dif is None:
                dif = -1 if old > x else 1

            if dif == 1 and old < x or dif == -1 and x < old:
                if abs(old - x) > 3 or old == x:
                    return False
            else:
                return False
        old = x

    return True


ans = 0

for line in f:
    n = [x for x in map(int, line.strip().split())]
    if check(n):
        ans += 1
    else:
        for i in range(len(n)):
            if check([n[j] for j in range(len(n)) if j != i]):
                ans += 1
                break

print(ans)
