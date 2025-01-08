input = open(0).readline

tmp = 1
n = int(input())

for i in range(1, 10000000):
    tmp += (6 * i)
    if n == 1:
        print(1)
        break
    elif n <= tmp:
        print(i+1)
        break
    else:
        i += 1