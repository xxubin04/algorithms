import sys
input = sys.stdin.readline

arr = []
for _ in range(n := int(input())):
    arr.append(list(map(int, input().split())))

visited = [0] * n
ans = int(1e9)

def calc():
    global ans

    morning = 0
    evening = 0

    for i in range(n):
        for j in range(n):
            if visited[i] and visited[j]:
                morning += arr[i][j]
            elif not visited[i] and not visited[j]:
                evening += arr[i][j]
    
    ans = min(ans, abs(morning - evening))

def dfs(idx, cnt):
    if cnt == n // 2:
        calc()
        return 
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1, cnt+1)
            visited[i] = 0

visited[0] = 1
dfs(1, 1)
print(ans)