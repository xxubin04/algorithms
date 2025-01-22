def num(N):
    if not N:
        return
    print(N)
    num(N-1)
    
n = int(input())
num(n)
