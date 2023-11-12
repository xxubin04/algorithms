S = int(input())
for s in range(S):
    a,b=map(str, input().split())
    a=int(a)
    bList=list(b)
    for i in range(len(b)):
        print(bList[i]*a, end="")
    print("")