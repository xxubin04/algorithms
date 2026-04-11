# 방향: 상, 하, 좌, 우, 대각선 (시계방향)
dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

N, M, K = map(int, input().split())

# board의 각 칸을 [파이어볼 개수, 질량의 합, 속력의 합, 방향들]로 설정
board = [[[0, 0, 0, []] for _ in range(N)] for _ in range(N)]  # 각 칸을 리스트로 초기화

fireballs = []

# 입력: 파이어볼의 초기 상태 설정
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])  # 0-based 인덱스 처리
    loc = board[r - 1][c - 1]
    loc[0] += 1  # 파이어볼 개수 증가
    loc[1] += m  # 질량 합 증가
    loc[2] += s  # 속도 합 증가
    loc[3].append(d)  # 방향 추가

# 파이어볼 이동 및 합치기
for _ in range(K):
    new_board = [[[0, 0, 0, []] for _ in range(N)] for _ in range(N)]  # 새 보드 초기화

    # 파이어볼 이동
    for r, c, m, s, d in fireballs:
        nr = (r + dirs[d][0] * s) % N
        nc = (c + dirs[d][1] * s) % N
        # 해당 칸에 새로운 파이어볼 추가
        new_board[nr][nc][0] += 1
        new_board[nr][nc][1] += m
        new_board[nr][nc][2] += s
        new_board[nr][nc][3].append(d)

    # 합치기
    fireballs = []
    for r in range(N):
        for c in range(N):
            count, m_sum, s_sum, dirs_list = new_board[r][c]
            if count >= 2:  # 2개 이상의 파이어볼이 합쳐지는 경우
                new_m = m_sum // 5  # 새로운 질량
                if new_m == 0:  # 질량이 0이면 사라짐
                    continue
                new_s = s_sum // count  # 속도 평균
                new_d = []
                if len(set([d % 2 for d in dirs_list])) == 1:  # 모든 방향이 짝수거나 홀수일 경우
                    new_d = [0, 2, 4, 6]  # 방향 (0, 2, 4, 6)
                else:
                    new_d = [1, 3, 5, 7]  # 방향 (1, 3, 5, 7)
                for d in new_d:
                    fireballs.append([r, c, new_m, new_s, d])  # 새로운 파이어볼 추가
            elif count == 1:  # 1개인 경우 그대로 유지
                fireballs.append([r, c, m_sum, s_sum, dirs_list[0]])

result = sum([f[2] for f in fireballs])  # 남아있는 파이어볼들의 질량 합
print(result)