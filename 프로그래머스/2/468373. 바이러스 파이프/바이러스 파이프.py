# 최대한 많은 배양체에 바이러스 감염 
# 한 종류의 파이프만 열 수 있음 
    
def solution(n, infection, edges, k):
    global graph, visited, max_infect
    
    max_infect = 0
    visited = [0] * (n+1)
    graph = {}
    
    for s, e, p in edges:  # 시작점, 도착점, 파이프 종류
        if s in graph:
            graph[s][e] = p
        else:
            graph[s] = {e: p}
            
        if e in graph:
            graph[e][s] = p
        else:
            graph[e] = {s: p}

    def dfs(cnt, infected, pipe):
        global max_infect
        max_infect = max(max_infect, len(infected))
        if cnt == k:  # 최대 방문횟수에 도달했다면
            return

        for next_pipe in range(1, 4):
            q = list(infected)
            new_infected = set(infected)
            for node in q:
                for end, p in graph.get(node, {}).items():
                    if p == next_pipe and end not in new_infected:
                        new_infected.add(end)
                        q.append(end)
                        
            if new_infected != infected:
                dfs(cnt+1, new_infected, next_pipe)
            
    dfs(0, {infection}, -1)
    return max_infect