import math
input = open(0).readline

l = int(input())
lamp = int(input())
locs = sorted(list(map(int, input().split())))
min_h = locs[0]

for i in range(len(locs)):
    if i == len(locs) - 1:
        if l - locs[i] > min_h:
            min_h = l - locs[i]
        break

    if locs[i] + min_h < locs[i+1] - min_h:
        min_h = math.ceil((locs[i+1] - locs[i]) / 2)

print(min_h)