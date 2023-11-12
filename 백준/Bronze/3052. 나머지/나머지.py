aList = []
for i in range(10):
    a = int(input())
    aList.append(a % 42)
print(len(set(aList)))