aList = []
for i in range(9):
    a = int(input())
    aList.append(a)
print(max(aList))
print(aList.index(max(aList))+1)