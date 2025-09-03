import sys

h, w, x, y = map(int, sys.stdin.readline().split())
nums = []

for _ in range(h+x):
    nums.append(list(map(int, sys.stdin.readline().split())))

array = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if i >= x and j >= y:
            array[i][j] = nums[i][j] - array[i-x][j-y]
        else:
            array[i][j] = nums[i][j]

for i in range(h):
    print(*array[i])