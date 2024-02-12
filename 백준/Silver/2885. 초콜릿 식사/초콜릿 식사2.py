input = open(0).readline

square = int(input())
size = 1

while size < square:
    size *= 2

i = size
cnt = 0

if square == size:
    print(size, 0)
else:
    while square != 0:
        square -= i if square >= i else 0
        i //= 2
        cnt += 1
    print(size, cnt-1)
