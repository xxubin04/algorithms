import sys

a, b, c = map(int, sys.stdin.readline().split())
print((a + b) % c)
print(((d := (a%c)) + (e := (b % c))) % c)
print((a * b) % c)
print((d * e) % c)