a,b = map(str, input().split())
aList = list(a[::-1])
bList = list(b[::-1])
a,b = "", ""
for i in range(len(aList)):
  a += aList[i]
  b += bList[i]
if int(a) > int(b) :
  print(a)
else:
  print(b)