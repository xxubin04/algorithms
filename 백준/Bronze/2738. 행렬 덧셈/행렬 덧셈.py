from sys import stdin as std

N, M = map(int, std.readline().split())
arrayA = []; arrayB = []
for _ in range(N):
    arrayA.append(list(map(int, std.readline().split())))
for _ in range(N):
    arrayB.append(list(map(int, std.readline().split())))

for n in range(N):
    for m in range(M):
        num = arrayA[n][m] + arrayB[n][m]
        print(num, end=' ')
    print("")