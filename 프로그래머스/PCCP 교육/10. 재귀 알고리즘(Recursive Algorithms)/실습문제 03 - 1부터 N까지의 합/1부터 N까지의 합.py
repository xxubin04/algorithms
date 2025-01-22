def num(N):
    if N == 0:
        return 0
    return N + num(N-1)
    
n = int(input())
print(num(n))
