def solution(k, dungeons):
    visited = [0] * len(dungeons)
    explore = 0  # 탐험할 수 있는 최댓값
    
    def dfs(fatigue, count):
        nonlocal explore
        explore = max(explore, count)
        
        for i in range(len(dungeons)):
            need, cost = dungeons[i]
            
            if not visited[i] and fatigue >= need:
                visited[i] = 1
                dfs(fatigue - cost, count+1)
                visited[i] = 0
    
    dfs(k, 0)
    return explore