N=int(input())
aList=list(map(int, input().split()))
aList.sort()
best=aList[N-1]
bList=[]
total=0
for i in range(N):
    bList.append(aList[i]/best*100)
for j in range(N):
    total+=bList[j]
print(round(total/N, 6))