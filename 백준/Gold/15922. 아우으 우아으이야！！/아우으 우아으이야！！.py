input = open(0).readline

n = int(input())
start, end = map(int, input().split())
total = 0

for i in range(n-1):
    x, y = map(int, input().split())

    if x <= end:
        end = max(end, y)
    else:
        total += (end - start)
        start, end = x, y

print(total + end - start)