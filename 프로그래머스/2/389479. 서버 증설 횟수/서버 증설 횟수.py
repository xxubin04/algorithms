def solution(players, m, k):
    cnt = 0
    valid_server = []  # 남은 시간들 저장 
    
    for p in players:
        n = (p - (m * len(valid_server))) // m

        for _ in range(n):
            valid_server.append(k)
            cnt += 1 
        
        s = 0
        while s < len(valid_server):
            valid_server[s] -= 1
            
            if valid_server[0] == 0:
                valid_server.pop(0)
            else:
                s += 1        
    
    return cnt 