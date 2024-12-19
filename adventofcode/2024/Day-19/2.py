f = open('input.txt', 'r')
lines = f.read().splitlines()
towels = lines[0].strip().split(', ')
checks = {}
summa = 0


def checkDesign(line):
    if line in checks.keys():
        return checks[line]
    ans = 0

    for towel in towels:
        if towel == line:
            ans += 1
        elif len(towel) <= len(line) and line[:len(towel)] == towel:
            ans += checkDesign(line[len(towel):])

    checks[line] = ans
    return ans


for i in range(2, len(lines)):
    summa += checkDesign(lines[i])

print(summa)
