def solution(n):
    # 시간초과 -> 중복계산
    # def fibo(a):
    #     if a == 0:
    #         return 0
    #     elif a == 1 or a == 2:
    #         return 1
    #     else:
    #         return fibo(a-2) + fibo(a-1)
    
    # 메모이제이션
#     memo = {}
    
#     def fibo(a):
#         if a == 0: return 0
#         if a == 1 or a == 2: return 1
#         if a in memo: return memo[a]
    
#         memo[a] = fibo(a-2) + fibo(a-1)
#         return memo[a]
    
    # DP
    if n == 0: return 0
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n] % 1234567