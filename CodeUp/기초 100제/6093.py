input = open(0).readline

n = int(input())
num = reversed(list(map(int, input().split())))

for i in num:
    print(i, end=" ")
