from collections import deque 

def solution(n, wires):
    min_diff = len(wires)  # 최소 차이 초기화
    graph = [[] for _ in range(n+1)]  # 1-based
    
    print(graph)
    
    for n1, n2 in wires:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    # 끊을 전선 순회
    for n1, n2 in wires:
        visited = [0] * (n+1)  # 노드 방문 여부
        
        q = deque([n1])
        
        while q:
            node = q.popleft()
            visited[node] = 1  # 방문처리
            
            for next_node in graph[node]:
                # 끊은 전선이라면 
                if (node == n1 and next_node == n2) or (node == n2 and next_node == n1):
                    continue
                    
                if not visited[next_node]:  # 아직 방문하지 않은 노드라면
                    q.append(next_node)
                    
        min_diff = min(min_diff, abs(n - 2 * sum(visited)))
    
    return min_diff