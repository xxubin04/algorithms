from sys import stdin

N, M = map(int, stdin.readline().split())
aList = [0]
for n in range(1, N+1):
    aList.append(n)

for _ in range(M):
    i, j = map(int, stdin.readline().split())
    aList[i:j+1] = aList[j:i-1:-1]

for k in range(1, N+1):
    print(aList[k], end=" ")