# def solution(triangle):
#     l = len(triangle)
#     dp = [[] for _ in range(l)]
#     dp[0] = triangle[0][:]
    
#     for r in range(1, l):
#         # for c in range(r + 1):
#         #     if c == 0:  # 왼쪽
#         #         dp[r].append(dp[r-1][0] + triangle[r][0])
#         #     elif c == r:  # 오른쪽
#         #         dp[r].append(dp[r-1][r-1] + triangle[r][r])
#         #     else:  # 중간
#         #         dp[r].append(max(dp[r-1][c-1], dp[r-1][c]) + triangle[r][c])
#         for c in range(r+1):
#             if c == 0:
#                 dp[r].append(dp[r-1][0] + triangle[r][0])
#             elif c == r:
#                 dp[r].append(dp[r-1][r-1] + triangle[r][r])
#             else:
#                 dp[r].append(max(dp[r-1][c-1], dp[r-1][c]) + triangle[r][c])
                
    
#     return max(dp[-1])



def solution(triangle):
    l = len(triangle)
    dp = [[] for _ in range(l)]
    dp[0] = triangle[0][:]
    
    for r in range(1, l):  # 자식 기준
        for c in range(r+1):
            if c == 0:
                dp[r].append(dp[r-1][0] + triangle[r][0])
            elif c == r:
                dp[r].append(dp[r-1][c-1] + triangle[r][r])
            else:
                dp[r].append(max(dp[r-1][c-1], dp[r-1][c]) + triangle[r][c])
    
    return max(dp[l-1])