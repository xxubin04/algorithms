def num(N):
    if not N:
        return
    num(N-1)
    print(N)
    
n = int(input())
num(n)
