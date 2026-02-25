n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for r in range(n):
    acc = 1
    prior = grid[r][0]
    for i in range(1, n):
        if grid[r][i] == prior:
            acc += 1 
        else:
            prior = grid[r][i]
            acc = 1

        if acc >= m:
                ans += 1 
                break

for c in range(n):
    acc = 1
    prior = grid[0][c]
    for i in range(1, n):
        if grid[i][c] == prior:
            acc += 1 
        else:
            prior = grid[i][c]
            acc = 1
        
        if acc >= m:
                ans += 1 
                break

print(ans)