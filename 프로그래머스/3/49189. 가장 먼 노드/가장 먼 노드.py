# from collections import deque

# def solution(n, edge):
#     graph = [[] for _ in range(n + 1)]

#     for a, b in edge:
#         graph[a].append(b)
#         graph[b].append(a)

#     distance = [-1] * (n + 1)
#     distance[1] = 0

#     q = deque([1])

#     while q:
#         cur = q.popleft()

#         for nxt in graph[cur]:
#             if distance[nxt] == -1:
#                 distance[nxt] = distance[cur] + 1
#                 q.append(nxt)

#     max_dist = max(distance)

#     return distance.count(max_dist)















from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    
    for i, j in vertex:
        graph[i].append(j)
        graph[j].append(i)
    
    distance = [-1, 0] + ([-1] * (n-1))
    
    q = deque([1])
    
    while q:
        n = q.popleft()
        
        for node in graph[n]:
            if distance[node] == -1:  # 아직 방문하지 않은 노드라면
                distance[node] = distance[n] + 1
                q.append(node)
    
    max_dist = max(distance)
    
    return distance.count(max_dist)