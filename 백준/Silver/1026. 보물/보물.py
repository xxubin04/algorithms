from sys import stdin

N = int(stdin.readline())
S = 0
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
A.sort(reverse=True); B.sort()
for i in range(N):
    S += A[i]*B[i]
print(S)