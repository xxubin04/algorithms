# from collections import deque

# def solution(n, computers):
#     answer = 0
#     visited = [0] * n
    
#     def bfs(m):
#         nonlocal visited, answer
#         q = deque([m])
        
#         while q:
#             node = q.popleft()
#             visited[node] = 1  # 방문처리
            
#             for i in range(n):
#                 if i == node:  # 자기 자신 노드라면
#                     continue
                
#                 if computers[node][i] and not visited[i]:  # 연결되어 있으면서 아직 방문하지 않은 노드라면
#                     q.append(i)  # 노드 추가
        
#         answer += 1  # 네트워크 1 추가
#         print(visited)
#         print(answer)
        
    
#     for j in range(n):
#         if not visited[j]:
#             bfs(j)
        
#     return answer











from collections import deque

def solution(n, computers):
    visited = [0] * n  # 0-based
    cnt = 0
    
    for node in range(n):
        if visited[node]:  # 이미 방문했다면 넘기기
            continue 
        
        q = deque([node])
        visited[node] = 1
        
        while q:
            node = q.popleft()
            
            for next_node in range(n):
                if computers[node][next_node] == 1:
                    if visited[next_node]:
                        continue 

                    visited[next_node] = 1  # 방문처리
                    q.append(next_node)
                
        cnt += 1
    
    return cnt