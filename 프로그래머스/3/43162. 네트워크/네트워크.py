from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    def bfs(m):
        nonlocal visited, answer
        q = deque([m])
        
        while q:
            node = q.popleft()
            visited[node] = 1  # 방문처리
            
            for i in range(n):
                if i == node:  # 자기 자신 노드라면
                    continue
                
                if computers[node][i] and not visited[i]:  # 연결되어 있으면서 아직 방문하지 않은 노드라면
                    q.append(i)  # 노드 추가
        
        answer += 1  # 네트워크 1 추가
        print(visited)
        print(answer)
        
    
    for j in range(n):
        if not visited[j]:
            bfs(j)
        
    return answer