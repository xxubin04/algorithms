# def solution(m, n, puddles):
#     route = [[0] * m for _ in range(n)]
    
#     for p in range(len(puddles)):
#         px, py = puddles[p]
#         puddles[p] = [px - 1, py - 1]
        
#     for x in range(n):
#         for y in range(m):
            
#             # 웅덩이
#             if [y, x] in puddles:
#                 continue 
            
#             # 시작점
#             if x == 0 and y == 0:
#                 route[0][0] = 1
#                 continue
                
#             # 첫 행
#             if x == 0:
#                 route[x][y] = route[x][y - 1]
#                 continue
                
#             # 첫 열
#             if y == 0:
#                 route[x][y] = route[x - 1][y]
#                 continue 
            
#             # 일반적인 경우
#             route[x][y] = (route[x - 1][y] + route[x][y - 1]) % 1000000007

#     return route[n - 1][m - 1]


def solution(m, n, puddles):
    route = [[0] * m for _ in range(n)]
    
    for pidx in range(len(puddles)):
        px, py = puddles[pidx]
        puddles[pidx] = [px-1, py-1]  # 0-based
    
    for x in range(n):  # 행
        for y in range(m):  # 열 
            
            # 웅덩이라면 넘김
            if [y, x] in puddles:
                continue 
            
            # 시작점 초기화
            if x == 0 and y == 0:
                route[0][0] = 1
                continue
            
            # 맨 위 행
            if x == 0:
                route[x][y] = route[x][y-1]
                continue
            
            # 맨 왼쪽 열
            if y == 0:
                route[x][y] = route[x-1][y]
                continue
            
            # 일반적인 경우
            route[x][y] = route[x][y-1] + route[x-1][y]
            
    return route[n-1][m-1] % 1000000007