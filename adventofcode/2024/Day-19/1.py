f = open('input.txt', 'r')
lines = f.read().splitlines()
towels = lines[0].strip().split(', ')
checks = {}
summa = 0


def checkDesign(line):
    if line in checks.keys():
        return checks[line]

    for towel in towels:
        if towel == line:
            return 1

        if len(towel) <= len(line) and line[:len(towel)] == towel:
            d = checkDesign(line[len(towel):])

            if d:
                checks[line] = 1
                return 1

    checks[line] = 0
    return 0


for i in range(2, len(lines)):
    summa += checkDesign(lines[i])

print(summa)