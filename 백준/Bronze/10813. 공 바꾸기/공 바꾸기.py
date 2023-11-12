N, M = map(int, input().split())
aList = []
for n in range(1, N+1):
    aList.append(n)
for m in range(M):
    i, j = map(int, input().split())
    aList[i-1], aList[j-1] = aList[j-1], aList[i-1]
for a in range(N):
    print(aList[a], end=" ")