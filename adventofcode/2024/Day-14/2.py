import re
from PIL import Image

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
        mp[self.x][self.y] = 1


robots = []

for line in f.read().split('\n'):
    if len(line.strip()) > 0:
        robots.append(Robot(line, 1000))
ii = 1001
while True:
    fail = False
    mp = [[0 for x in range(py)] for y in range(px)]

    for robot in robots:
        robot.step(1)

    height = len(mp)
    width = len(mp[0])

    image = Image.new("RGB", (width, height), "black")
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            if mp[y][x] == 0:
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)
    image.save(f'map/{ii}.png')

    ii += 1

    if ii > 10000:
        break

# 7687
