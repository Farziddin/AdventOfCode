f = open('input.txt', 'r')
summa = 0

for line in f:
    i = 0

    while i < len(line):
        if '0' <= line[i] <= '9':
            summa += int(line[i]) * 10
            break

        i += 1

    i = len(line) - 1

    while i >= 0:
        if '0' <= line[i] <= '9':
            summa += int(line[i])
            break

        i -= 1

print(summa)
