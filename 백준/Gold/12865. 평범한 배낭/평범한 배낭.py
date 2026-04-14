import sys
input = sys.stdin.readline 

N, K = map(int, input().split())  # 물품의 수 N, 준서가 버틸 수 있는 무게 K
dp = [[0] * (K+1) for _ in range(N+1)]
things = [(0,0)]

for _ in range(N):
    things.append(tuple(map(int, input().split())))  # 물건의 무게 W, 물건의 가치 V

for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = things[i][0], things[i][1]  # 물건의 무게 W, 물건의 가치 V

        if w > j:  # 물건의 무게 > 배낭의 남은 무게
            dp[i][j] = dp[i-1][j]
        else:  # 물건의 무게 <= 배낭의 남은 무게 
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])
    
print(dp[N][K])