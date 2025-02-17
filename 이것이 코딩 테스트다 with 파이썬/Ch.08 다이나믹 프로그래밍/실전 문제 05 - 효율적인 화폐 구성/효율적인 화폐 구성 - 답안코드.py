n, m = map(int, input().split())
money = []
for i in range(n):
    money.append(int(input()))

d = [10001] * (m+1)

# Bottom-Up 방식으로 DP 진행
d[0] = 0
for i in range(n):
    for j in range(money[i], m+1):
        if d[j - money[i]] != 10001:  # (i - k)원을 만든느 방법이 존재한다면
            d[j] = min(d[j], d[j - money[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
