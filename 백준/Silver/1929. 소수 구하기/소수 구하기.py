import sys

n, m = map(int, sys.stdin.readline().split())

def prime_numbers(m):
    arr = [k for k in range(m+1)]
    end = int(m ** (1/2))
    for j in range(2, end+1):
        if arr[j] == 0:
            continue
        for p in range(j*j, m+1, j):
            arr[p] = 0

    arr[1] = 0
    return arr

primes = prime_numbers(m)

for i in range(n, m+1):
    if primes[i]:
        print(i)