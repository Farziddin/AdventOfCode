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
    p['x'] += 10000000000000
    p['y'] += 10000000000000
    t1 = p['x'] * b['y'] - p['y'] * b['x']
    t2 = a['x'] * b['y'] - a['y'] * b['x']

    if t1 % t2 > 0:
        return 0

    i = t1 // t2

    if (p['x'] - a['x'] * i) % b['x'] > 0:
        return 0

    return i * 3 + (p['x'] - a['x'] * i) // b['x']


i = 0
summa = 0

while i < len(lines):
    summa += get(getXY(lines[i]), getXY(lines[i + 1]), getXY(lines[i + 2]))
    i += 4

print(summa)
