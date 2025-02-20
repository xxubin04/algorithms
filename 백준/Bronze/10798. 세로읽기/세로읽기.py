array = []
l = 0

for i in range(5):
    array.append(a := list(input().rstrip()))
    if len(a) > l:
        l = len(a)

for j in range(l):
    for k in range(5):
        if len(array[k]) >= j+1:
            print(array[k][j], end='')