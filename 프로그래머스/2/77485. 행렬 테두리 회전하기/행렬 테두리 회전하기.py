from collections import deque

def solution(rows, columns, queries):
    answer = []
    grid = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    
    for q in queries:
        min_value = float('inf')
        r1, c1, r2, c2 = q
        r1 -= 1
        c1 -= 1
        r2 -= 1
        c2 -= 1  # 1-based
        
        temp = [grid[r1][c2], grid[r2][c2], grid[r2][c1]]
        
        # 오른쪽으로 이동 
        for c in range(c2-1, c1-1, -1):
            grid[r1][c+1] = (g := grid[r1][c])  # 오른쪽으로 1칸씩 옮기기
            if g < min_value:
                min_value = g
        
        # 아래쪽으로 이동
        for r in range(r2-1, r1, -1):
            grid[r+1][c2] = (g := grid[r][c2])  # 아래로 1칸씩 옮기기
            if g < min_value:
                min_value = g
        
        # 왼쪽으로 이동
        for c in range(c1+1, c2+1):
            grid[r2][c-1] = (g := grid[r2][c])  # 왼쪽으로 1칸씩 옮기기
            if g < min_value:
                min_value = g
        
        # 위쪽으로 이동
        for r in range(r1+1, r2):
            grid[r-1][c1] = (g := grid[r][c1])  # 아래로 1칸씩 옮기기
            if g < min_value:
                min_value = g
        
        grid[r1+1][c2] = (g := temp[0])
        if g < min_value:
            min_value = g
                
        grid[r2][c2-1] = (g := temp[1])
        if g < min_value:
            min_value = g
                
        grid[r2-1][c1] = (g := temp[2])
        if g < min_value:
            min_value = g

        answer.append(min_value)
    
    return answer