import re

from cffi.cffi_opcode import PRIM_INT

f = open('input.txt', 'r')
lines = f.read().split('\n')


def getXY(txt):
    nums = re.findall(r'-?\d+', txt)

    return {
        'x': int(nums[0]),
        'y': int(nums[1]),
    }


def get(a, b, p):
    ans = 0

    for i in range(p['x'] // a['x'] + 1):
        r = (p['x'] - a['x'] * i) // b['x']

        if a['x'] * i + b['x'] * r == p['x'] and a['y'] * i + b['y'] * r == p['y']:
            if ans == 0 or i * 3 + r < ans:
                ans = i * 3 + r

    return ans


i = 0
summa = 0

while i < len(lines):
    summa += get(getXY(lines[i]), getXY(lines[i + 1]), getXY(lines[i + 2]))
    i += 4

print(summa)
