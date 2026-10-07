from collections import deque

K, M = map(int, input().split())  # K: 탐사의 반복 횟수 / M: 유물 조각의 개수 

grid = [list(map(int, input().split())) for _ in range(5)]
wall = deque(list(map(int, input().split())))  # 벽면에 적힌 유물 조각 번호들
same_value_case = []  # 유물 1차 획득 가치가 동일한 케이스들 전부 저장 [(좌상의 좌표), 회전각도, [(회전한 좌표의 유물 가치 리스트)], 합쳐진 좌표 리스트]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# 시계방향으로 90도 회전
def rotate_90(matrix):
    rotate_matrix = [list(row) for row in zip(*matrix[::-1])]

    return rotate_matrix


# 유물 가치 계산 (BFS)
def cal_value(matrix):
    visited = [[0] * 5 for _ in range(5)]  # 방문여부
    remove_visited = [[0] * 5 for _ in range(5)]

    total = 0  # 모든 유물들의 가치 합

    for x in range(5):
        for y in range(5):
            visited_cell = []  

            if visited[x][y] != 0:
                continue

            num = matrix[x][y]

            visited[x][y] = 1  # 방문처리
            visited_cell.append((x, y))  # 방문한 좌표들 저장 

            q = deque([(x, y)])  # 아직 방문하지 않은 좌표만 방문 

            while q:
                cx, cy = q.popleft()

                for dx, dy in dirs:
                    nx, ny = cx + dx, cy + dy 

                    if not 0 <= nx < 5:
                        continue
                    
                    if not 0 <= ny < 5:
                        continue 
                    
                    if visited[nx][ny]:
                        continue 
                    
                    if matrix[nx][ny] != num:  # 같은 유물 번호여야 연결할 수 있음
                        continue 
                    
                    visited[nx][ny] = 1  # 방문처리
                    q.append((nx, ny))  # 해당 좌표 큐에 넣기
                    visited_cell.append((nx, ny))  # 방문한 좌표 저장
            
            cnt = len(visited_cell)

            if cnt >= 3:
                total += cnt  # 각 유물의 합을 최종 합에 더함 
                
                for i, j in visited_cell:
                    # 실제로 제거될 좌표만 따로 체크
                    remove_visited[i][j] = 1
    
    return (total, remove_visited)


# [1. 탐사 진행] 회전 목표를 만족하는 (좌표 + 회전 수) 선택
#   1) 유물 1차 획득 가치 최대화
#   2) 회전 각도 최소화
#   3) 열 작게, 행 작게
def choose_by_goal():
    max_value = 0  # 유물 1차 획득 가치의 초기값 0
    same_value_case = []

    # 3x3 격자 선택 (좌상단 좌표 = (r, c))
    for c in range(3):  # 열이 작은 순서 > 행이 작은 순서
        for r in range(3):

            matrix = [row[c:c+3] for row in grid[r:r+3]]
            
            # 90, 180, 270도 회전
            for i in range(1, 4):

                # 3x3 matrix 자체만 계속 90도 회전
                matrix = rotate_90(matrix)

                # 전체 격자 복사
                rotate_grid = [row[:] for row in grid]

                # 회전한 3x3 부분만 전체 격자에 적용
                for x in range(3):
                    for y in range(3):
                        rotate_grid[r+x][c+y] = matrix[x][y]
                
                # 이번 좌표의 경우가 최대 유물 가치의 합보다 크다면
                # 최댓값 갱신 + same_value_case 초기화
                total, visited = cal_value(rotate_grid)

                if total > max_value:
                    same_value_case = [[(r, c), i, rotate_grid, visited]]
                    max_value = total 

                # 이번 좌표의 경우가 최대 유물 가치의 합과 같다면
                # same_value_case에 추가
                elif total == max_value:
                    same_value_case.append([(r, c), i, rotate_grid, visited])

                # 이번 좌표의 경우가 최대 유물 가치의 합보다 작다면, 무시
    
    # 유물 가치의 합이 같은 조합들 중에서
    # 회전 횟수가 가장 작고
    # 열이 작고, 행이 작은 조합으로 선택

    # 오름차순으로 회전각 -> 열 -> 행
    same_value_case.sort(key=lambda x: (x[1], x[0][1], x[0][0]))

    matrix = same_value_case[0][2]
    visited = same_value_case[0][3]
                
    return (matrix, visited, max_value)           


# 벽면 조각으로 갱신
def renew_by_wall(visited):

    # 열 번호가 작은 순서
    for j in range(5):
        # 같은 열이라면 행 번호가 큰 순서
        for i in range(4, -1, -1):
            if visited[i][j] == 1:  # 제거된 유물 위치에 새로운 조각으로 갱신
                grid[i][j] = wall.popleft()


# [메인]
# K번 탐사 진행
for _ in range(K):

    total_by_turn = 0  # 턴마다의 가치 총합

    matrix, visited, max_value = choose_by_goal()  # 목표를 만족하도록 회전한 격자, 새로 갱신해야 하는 좌표

    # 유물 획득 불가라면 전체 탐사 종료
    if max_value == 0:
        break

    # 회전한 격자로 실제 grid 갱신
    grid = [row[:] for row in matrix]
    total_by_turn += max_value

    # 제거된 위치들을 벽면의 조각으로 갱신
    renew_by_wall(visited)

    while True:
        value, visited = cal_value(grid)

        # 더 이상 유물을 획득할 수 없다면 이번 턴 종료
        if value == 0:
            break

        total_by_turn += value
        renew_by_wall(visited)

    print(total_by_turn, end=' ')