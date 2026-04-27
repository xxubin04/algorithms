def solution(n):
    cnt = 0
    for i in range(1, n+1):
        ssum = 0
        while ssum < n:
            ssum += i
            i += 1
        if ssum == n:
            cnt += 1
            
    return cnt