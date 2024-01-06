input = open(0).readline

n = int(input())
nList = sorted(list(map(int, input().split())))
goal = int(input())

cnt = 0; start = 0; end = n-1

while start < end:
    temp = nList[start] + nList[end]
    if temp == goal:
        cnt += 1
        start += 1
    elif temp < goal:
        start += 1
    else:
        end -= 1
print(cnt)