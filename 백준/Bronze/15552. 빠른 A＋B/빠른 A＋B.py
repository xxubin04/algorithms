from sys import stdin

num = int(stdin.readline())
for i in range(num):
    A, B = map(int, stdin.readline().rstrip().split())
    C = A + B
    print(C)