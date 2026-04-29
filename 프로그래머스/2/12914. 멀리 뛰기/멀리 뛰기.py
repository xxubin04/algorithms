def solution(n):
    dp = [0, 1, 2] + [0] * (n-2)
    
    for i in range(3, n+1):
        # dp[i]에 도달하는 방법은 2가지이다.
        # 1) dp[i-1]에서 1칸 멀리 뛰기 (1번)
        # 2) dp[i-2]에서 2칸 멀리 뛰기 (1번)
        # 따라서 dp[i]로의 경로는 dp[i-1] + dp[i-2]이다.
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567