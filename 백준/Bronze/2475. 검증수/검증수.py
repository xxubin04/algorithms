def double(j):
    global num
    num = j**2
    return num

aList = list(map(int, input().split()))
total = 0
global num
for i in aList:
    total += double(i)

print(total%10)