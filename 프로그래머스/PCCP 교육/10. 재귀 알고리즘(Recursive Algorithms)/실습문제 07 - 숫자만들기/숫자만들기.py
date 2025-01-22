def f(N, K, digit, max_st, st):
    if st != "" and int(st) > N:
        return max_st
    
    if st != "" and int(st) <= N:
        max_st = max(max_st, int(st))
    
    for j in range(K):
        max_st = f(N, K, digit + 1, max_st, st + Q[j])
    
    return max_st

N, K = map(int, input().split())
Q = list(map(str, input().split()))

print(f(N, K, 0, 0, ""))
