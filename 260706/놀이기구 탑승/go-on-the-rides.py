n = int(input())
like_list = {}  # 좋아하는 친구들 해시에 저장 
p_seq = []  # 놀이기구 타는 순서
dirs = [(0,1), (0,-1), (1,0), (-1,0)]  # 동서남북
score = 0  # 점수 

for _ in range(n*n):
    p, l1, l2, l3, l4 = map(int, input().split())
    like_list[p] = [l1, l2, l3, l4]
    p_seq.append(p)

board = [[0] * n for _ in range(n)]  # 탑승 위치 (처음에 0으로 초기화)

for p in p_seq:  # 놀이기구에 타는 순서대로 순회
    # 1) 좋아하는 친구가 많은 곳
    candidates = []  # (좋아하는 친구 수, 인접한 빈 칸 수, 행, 열) 저장 
    ll = like_list[p]  # 좋아하는 친구 리스트 
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:  # 빈 칸일 경우
                f_cnt = 0  # 좋아하는 친구 수 
                b_cnt = 0  # 빈 칸 수 
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:  # 범위 안
                        if board[nx][ny] in ll:  # 친구가 있는 경우 
                            f_cnt += 1
                        elif board[nx][ny] == 0:  # 빈 칸인 경우 
                            b_cnt += 1
                candidates.append((f_cnt, b_cnt, x, y))  # (좋아하는 친구 수, 빈 칸 수, 행, 열) 저장 
            
    candidates.sort(key = lambda x: (-x[0], -x[1], x[2], x[3]))
    nx, ny = candidates[0][2], candidates[0][3]
    board[nx][ny] = p

for x in range(n):
    for y in range(n):
        ll = like_list[board[x][y]]
        cnt = 0  # 좋아하는 친구의 수 
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in ll:
                cnt += 1
        
        score += (10 ** cnt // 10)
print(score)