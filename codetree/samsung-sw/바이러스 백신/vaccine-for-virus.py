from collections import deque

n, m = map(int, input().split())
graph = []
hospital = []  # 병원 좌표 
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
empty_count = 0  # 0의 개수

for i in range(n):
    graph.append(row := list(map(int, input().split())))

    for j in range(n):
        if row[j] == 2:
            hospital.append((i, j))
        elif row[j] == 0:
            empty_count += 1

comb = []
def combination(start, depth, selected):
    if depth == m:
        comb.append(selected[:])
        return 

    for i in range(start, len(hospital)):
        selected.append(hospital[i])
        combination(i+1, depth+1, selected)
        selected.pop()

# 조합 
combination(0, 0, [])

def bfs(c):
    # 얕은 복사 
    temp = [[] for _ in range(n)]
    for i in range(n):
        temp[i] = graph[i][:] 

    q = deque(c)  # 병원 조합으로 덱 초기화 
    max_time = 0
    remain = empty_count  # 0 남은 개수

    for hos in c:  # 방문할 병원들 먼저 -1로 초기화 
        temp[hos[0]][hos[1]] = -1

    while q:
        x, y = q.popleft()
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and (tmp := temp[nx][ny]) in [0, 2]:
                temp[nx][ny] = (max_time := temp[x][y] - 1)
                q.append((nx, ny))

                if tmp == 0:
                    remain -= 1

            if not remain:  # 남은 바이러스가 없다면
                return max_time

    if remain:  # 바이러스가 남았다면
        return 1
        
    return max_time

min_time = float('-inf')  # 바이러스 전부 없애는 최소 시간

for c in comb:
    if (t := bfs(c)) != 1:
        min_time = max(min_time, t)
        
if min_time == float('-inf'):
    print(-1)
elif min_time == 0:
    print(0)
else:
    print(min_time * (-1) - 1)