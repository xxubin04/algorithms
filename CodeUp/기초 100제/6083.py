﻿input = open(0).readline

cnt = 0
r, g, b = map(int, input().split())

for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
            cnt += 1

print(cnt)
