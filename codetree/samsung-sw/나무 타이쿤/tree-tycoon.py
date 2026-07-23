from collections import deque

n, m = map(int, input().split())
height = []  # 높이 
rule = []  # 이동규칙
potion = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])  # 영양제 위치
inc_height = {}  # 좌표마다 증가해야 할 높이 저장
dir1 = [(), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
dir2 = [(-1, 1), (-1, -1), (1, 1), (1, -1)]  # 대각선 방향

for _ in range(n):
    height.append(list(map(int, input().split())))

for _ in range(m):
    rule.append(list(map(int, input().split())))

for d, p in rule:
    lp = len(potion)
    for i in range(lp):

        dx = (potion[i][0] + dir1[d][0] * p + n) % n
        dy = (potion[i][1] + dir1[d][1] * p + n) % n

        height[dx][dy] += 1  # 영양제 투입 후, 높이 1 증가 
        potion[i] = ((dx, dy))

    inc_height = {} 
    prior = set(potion)

    while potion:
        x, y = potion.popleft()
        cnt = 0  # 대각선의 인접 나무 개수

        for i in range(4):
            dx, dy = x +dir2[i][0], y + dir2[i][1]

            if 0 <= dx < n and 0 <= dy < n:
                if height[dx][dy] >= 1:
                    cnt += 1
        
        inc_height[(x, y)] = cnt
    
    # 대각선 인접 나무 개수만큼 높이 증가 
    for loc, inc in inc_height.items():
        height[loc[0]][loc[1]] += inc
    
    # 높이 2 이상의 나무들 영양제 주입
    for i in range(n):
        for j in range(n):
            if height[i][j] >= 2 and (i, j) not in prior:
                height[i][j] -= 2
                potion.append((i, j))

print(sum(val for row in height for val in row))