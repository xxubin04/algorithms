input = open(0).readline

road = []
for i in range(10):
    road.append(list(map(int, input().split())))

r, c = 1, 1
while True:
    if road[r][c] == 2:
        road[r][c] = 9
        break

    road[r][c] = 9
    if c+1 < 10 and road[r][c+1] == 0:
        c += 1
    elif r+1 < 10 and road[r+1][c] == 0:
        r += 1
    elif road[r+1][c] == 2:
        road[r+1][c] = 9
    elif road[r][c+1] == 2:
        road[r][c+1] = 9
    else:
        break

for i in range(10):
    for j in range(10):
        print(road[i][j], end=" ")
    print("")
