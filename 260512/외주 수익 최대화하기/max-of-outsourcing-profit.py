time = []
money = []

for _ in range(n := int(input())):
    a, b = map(int, input().split())
    time.append(a)
    money.append(b)

dp = [0] * (n+1)

for i in range(n):
    # 오늘 일 안하는 경우
    dp[i+1] = max(dp[i+1], dp[i])

    # 오늘 일 하는 경우
    end = i + time[i]

    if end <= n:
        dp[end] = max(dp[end], dp[i] + money[i])

print(dp[n])