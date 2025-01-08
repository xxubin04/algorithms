import math as m
input = open(0).readline

H, W, N, M = map(int, input().split())
print(m.ceil(W/(M+1)) * m.ceil(H/(N+1)))