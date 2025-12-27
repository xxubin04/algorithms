import sys 

a, b, c = map(int, sys.stdin.readline().split())
if a == (m := min(a, b, c)):
    print(1, end=' ')
else:
    print(0, end=' ')

if max(a, b, c) == m:
    print(1)
else:
    print(0)