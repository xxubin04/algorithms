input = open(0).readline

a, m, d, n = map(int, input().split())

for i in range(n-1):
    a = a * m + d
print(a)
