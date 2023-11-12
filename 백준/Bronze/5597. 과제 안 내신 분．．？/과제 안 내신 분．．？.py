aList = []
bList = []
for i in range(28):
    a = int(input())
    aList.append(a)
for j in range(1, 31):
    bList.append(j)
cList = set(bList) - set(aList)
print(min(cList))
print(max(cList))
