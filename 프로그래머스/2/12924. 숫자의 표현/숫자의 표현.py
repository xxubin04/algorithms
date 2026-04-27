def solution(n):
    cnt = 0
    start, end = 1, 1
    while start <= n:
        total = (start + end) * (end - start + 1) / 2
        if total == n:
            cnt += 1
            start += 1
            end += 1
        elif total < n:
            end += 1
        else:
            start += 1
    
    return cnt