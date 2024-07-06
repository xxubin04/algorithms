input = open(0).readline

N = int(input())
while (N != 1):
    if N % 2 == 0:
        N /= 2
    else:
        print(0)
        exit()
print(1)