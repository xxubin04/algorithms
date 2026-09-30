def solution(m, n, puddles):
    route = [([0] * m) for _ in range(n)]
    
    for p in range(len(puddles)):
        px, py = puddles[p]
        puddles[p] = [px-1, py-1]
        
    for x in range(n):
        for y in range(m):
            if [y, x] in puddles:  # 물이 잠긴 지역이라면
                continue 
            
            if x == 0 and y == 0:
                route[0][0] = 1
                continue
                
            if x == 0 and y > 0:  # 맨 위면
                if y > 0 and [y-1, x] in puddles:
                    continue
                route[0][y] = route[0][y-1]
                continue
                
            if y == 0 and x > 0:  # 맨 왼쪽이면
                if x > 0 and [y, x-1] in puddles:
                    continue
                route[x][0] = route[x-1][0]
                continue 
            
            route[x][y] = route[x-1][y] + route[x][y-1]

    return route[n-1][m-1] % 1000000007
                
                