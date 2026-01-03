import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))

    max_price = 0
    ans = 0

    for i in range(n-1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            ans += max_price - prices[i]

    print(ans)