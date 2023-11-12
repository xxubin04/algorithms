a,b = map(int, input().split())
aList = list(map(int, input().split()))
for i in aList:
    if i < b:
        print(i, end=" ")
    else:
        continue