n, m = map(int, input().split())
board = []
people = []  # 사람의 좌표
hospital = [0]  # 병원의 좌표 
min_total = float('inf')  # 거리의 최솟값  

for i in range(n):
    board.append(l := list(map(int, input().split())))
    for j in range(n):
        if l[j] == 1:  # 사람이라면 
            people.append((i, j))
        elif l[j] == 2:  # 병원이라면
            hospital.append((i, j))
        
visited = [1] + [0] * (len(hospital)-1)  

def dfs(node, cnt):
    global min_total

    if cnt == m:
        total = 0

        for px, py in people:  # 사람의 좌표
            min_dist = float('inf')
            
            for i in range(1, len(visited)):
                if visited[i]:
                    hx, hy = hospital[i]
                    min_dist = min(min_dist, abs(hx-px) + abs(hy-py))

            total += min_dist  # 각 사람마다 병원까지의 최소 거리 

        min_total = min(min_total, total)
        return 
    
    for i in range(node, len(hospital)):
        if not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0

dfs(0, 0)
print(min_total)