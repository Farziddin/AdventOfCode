import re

f = open('input.txt', 'r')
px = 101
py = 103

mp = [[0 for x in range(py)] for y in range(px)]


class Robot:
    def __init__(self, line, step: int = None):
        self.x, self.y, self.i, self.j = re.findall(r'-?\d+', line)

        self.x = int(self.x)
        self.y = int(self.y)
        self.i = int(self.i)
        self.j = int(self.j)

        if step is not None:
            self.step(step)

    def step(self, x):
        self.x = (self.x + x * self.i) % px
        self.y = (self.y + x * self.j) % py
        mp[self.x][self.y] += 1


robots = []

for line in f.read().split('\n'):
    if len(line.strip()) > 0:
        robots.append(Robot(line, 100))

a = [0, 0, 0, 0]
for robot in robots:
    if robot.x == px // 2 or robot.y == py // 2:
        continue

    if 0 <= robot.x < px // 2:
        if 0 <= robot.y < py // 2:
            a[0] += 1
        else:
            a[2] += 1
    else:
        if 0 <= robot.y < py // 2:
            a[1] += 1
        else:
            a[3] += 1

summa = 1
for x in a:
    summa *= x

print(summa)
