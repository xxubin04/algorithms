N, M = map(int, input().split())
aList = []
for a in range(N):
    aList.append(0)
for p in range(M):
    i,j,k = map(int, input().split())
    for P in range(j-i+1):
        aList[i-1+P] = k

for q in range(N):
    print(aList[q], end=" ")
