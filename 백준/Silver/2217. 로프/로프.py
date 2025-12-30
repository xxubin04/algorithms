import sys

n = int(sys.stdin.readline())
weights = [int(sys.stdin.readline()) for _ in range(n)]

weights.sort()

max_weight = 0
for i in range(n):
    w = weights[i] * (n - i)
    if w > max_weight:
        max_weight = w

print(max_weight)