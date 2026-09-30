def solution(m, n, puddles):
    route = [[0] * m for _ in range(n)]
    
    for p in range(len(puddles)):
        px, py = puddles[p]
        puddles[p] = [px - 1, py - 1]
        
    for x in range(n):
        for y in range(m):
            
            # 웅덩이
            if [y, x] in puddles:
                continue 
            
            # 시작점
            if x == 0 and y == 0:
                route[0][0] = 1
                continue
                
            # 첫 행
            if x == 0:
                route[x][y] = route[x][y - 1]
                continue
                
            # 첫 열
            if y == 0:
                route[x][y] = route[x - 1][y]
                continue 
            
            # 일반적인 경우
            route[x][y] = (route[x - 1][y] + route[x][y - 1]) % 1000000007

    return route[n - 1][m - 1]