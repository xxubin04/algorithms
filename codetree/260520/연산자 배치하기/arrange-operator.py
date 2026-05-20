n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

min_op, max_op = int(1e9), -int(1e9)

def dfs(idx, value):
    global min_op, max_op
    
    if idx == n:
        min_op = min(min_op, value)
        max_op = max(max_op, value)
        return 
    
    for op in range(3):
        if ops[op] > 0:
            ops[op] -= 1
            match (op):
                case 0:
                    dfs(idx+1, value+nums[idx])
                case 1:
                    dfs(idx+1, value-nums[idx])
                case 2:
                    dfs(idx+1, value*nums[idx])
            ops[op] += 1

dfs(1, nums[0])
print(min_op, max_op)
