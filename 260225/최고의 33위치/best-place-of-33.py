n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_coin = 0

for y in range(n-2):
    for x in range(n-2):
        coin = grid[y][x] + grid[y][x+1] + grid[y][x+2] \
        + grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2] \
        + grid[y+2][x] + grid[y+2][x+1] + grid[y+2][x+2]
        
        if coin > max_coin:
            max_coin = coin

print(max_coin)