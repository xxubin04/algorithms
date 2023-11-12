a = int(input())
b = input()
bList = list(map(int, b))
c = a * bList[2]
d = a * bList[1]
e = a * bList[0]
f = c + d * 10 + e * 100
print(c)
print(d)
print(e)
print(f)