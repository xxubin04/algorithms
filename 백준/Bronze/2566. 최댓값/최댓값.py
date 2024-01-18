input = open(0).readline
arr = []
MAX2 = 0
for i in range(9):
    arr.append(list(map(int, input().split())))
    MAX1 = max(arr[i])
    MAX2 = max(MAX2, MAX1)
for j in range(9):
    for k in range(9):
        if arr[j][k] == MAX2:
            print(MAX2); print(j+1, k+1)
            break
        else:
            continue