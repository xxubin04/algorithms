import sys

area = 0
points = []

for _ in range(4):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y2-y1):
        for j in range(x2-x1):
            if (x1+j, y1+i) not in points:
                points.append((x1+j, y1+i))
                area += 1

print(area)