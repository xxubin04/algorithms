input = open(0).readline

n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
max_num, min_num = float("-inf"), float("inf")

def dfs(idx, current, plus, minus, mul, div):
    global max_num, min_num

    if idx == n:
        max_num = max(max_num, current)
        min_num = min(min_num, current)
        return

    if plus > 0:
        dfs(idx + 1, current + nums[idx], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, current - nums[idx], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, current * nums[idx], plus, minus, mul - 1, div)
    if div > 0:
        if current < 0:
            dfs(idx + 1, -(-current // nums[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, current // nums[idx], plus, minus, mul, div - 1)

dfs(1, nums[0], plus, minus, mul, div)
print(f"{max_num}\n{min_num}")