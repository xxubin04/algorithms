def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    
    dp[0] = land[0][:]
    
    for r in range(1, n):
        for c in range(4):  # 현재 열 
            for k in range(4):  # 이전 행의 열
                if c == k:
                    continue   # 같은 열은 선택 불가 
                
                dp[r][c] = max(dp[r][c], dp[r-1][k] + land[r][c])
    
    return max(dp[-1])