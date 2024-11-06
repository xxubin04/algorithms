input = open(0).readline

a = int(input())
i = 1
sum = 0

while 1:
    sum += i
    i += 1
    if sum >= a:
        print(sum)
        break
