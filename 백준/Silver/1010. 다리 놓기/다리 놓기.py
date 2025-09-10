import sys

def fact(n):
    if n <= 1:
        return 1
    else:
        return fact(n-1) * n

for _ in range(int(sys.stdin.readline().rstrip())):
    l, r = map(int, sys.stdin.readline().split())
    print(fact(r) // (fact(r-l) * fact(l)))