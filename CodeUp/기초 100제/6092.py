input = open(0).readline

num = [0 for _ in range(23)]
n = int(input())
check = list(map(int, input().split()))

for i in check:
    num[i-1] += 1

for j in num:
    print(j, end=" ")
