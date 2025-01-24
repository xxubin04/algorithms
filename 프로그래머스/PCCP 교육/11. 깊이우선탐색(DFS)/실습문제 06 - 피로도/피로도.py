def dfs(fatigue, cnt, visited, dungeons):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    
    for i in range(len(dungeons)):
        if not visited[i] and dungeons[i][0] <= fatigue:  
            visited[i] = 1
            dfs(fatigue - dungeons[i][1], cnt + 1, visited, dungeons) 
            visited[i] = 0 


def solution(k, dungeons):
    global max_cnt
    max_cnt = 0
    visited = [0 for _ in range(len(dungeons))]  
    dfs(k, 0, visited, dungeons)  
    
    return max_cnt
