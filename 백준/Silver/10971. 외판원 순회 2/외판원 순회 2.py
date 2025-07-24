import sys

dist = []  # 도시 간의 거리 저장 

def shortestPath(path, visited, currentLength):
    if len(path) == n:  # 모든 도시를 순회했다면 
        if dist[path[-1]][path[0]] == 0:  # 갈 수 없는 경로라면 
            return float('inf')
        return currentLength + dist[path[-1]][path[0]]

    ret = float('inf')

    for next in range(n):
        if visited[next]:  # 이미 방문한 도시라면 패스 
            continue

        if dist[path[-1]][next] == 0:  # 갈 수 없는 경로라면 패스
            continue

        here = path[-1]  # 현재 위치한 도시 
        path.append(next)  # 다음 방문한 도시를 경로에 추가 
        visited[next] = True  # 방문 처리 

        cand = shortestPath(path, visited, currentLength + dist[here][next])

        ret = min(ret, cand)  # 최소 거리 갱신 
        visited[next] = False  # 방문 미처리 
        path.pop()  # 경로에서 해당 도시 뺴냄 (백트래킹)

    return ret

for _ in range(n := int(sys.stdin.readline().strip())):
    dist.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [True] + [False] * (n-1)
path = [0]  # 경로에 시작 도시로 초기화

print(shortestPath(path, visited, 0))