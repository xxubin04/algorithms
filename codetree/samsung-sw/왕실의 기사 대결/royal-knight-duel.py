from collections import defaultdict

L, N, Q = map(int, input().split())  # L: 체스판 크기 / N: 기사 수 / Q: 왕의 명령 수

chessboard = []
knight = defaultdict(list)  # 기사가 차지하는 모든 좌표 저장
health = [0]  # 기사의 체력 저장 (1-based)
damaged = [0] * (N + 1)  # 기사마다 받은 대미지 저장 (1-based)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 위 오 아 왼

# 체스판 정보
for _ in range(L):
    chessboard.append(list(map(int, input().split())))

# 0: 빈칸 / 1: 함정 / 2: 벽
terrain = [row[:] for row in chessboard]

# 기사의 정보 체스판에 기록
for num in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    health.append(k)

    for i in range(r - 1, r + h - 1):
        for j in range(c - 1, c + w - 1):
            chessboard[i][j] = -num
            knight[num].append([i, j])


# 연쇄적으로 밀려야 하는 기사들이 전부 밀릴 수 있는지 확인
def can_push(i, d):
    # 이미 확인한 기사라면 다시 검사할 필요 없음
    if i in push_check:
        return True

    push_check.add(i)
    push_knight.append(i)

    dx, dy = dirs[d]

    for x, y in knight[i]:
        nx, ny = x + dx, y + dy

        # 범위 밖
        if not (0 <= nx < L and 0 <= ny < L):
            return False

        if terrain[nx][ny] == 2:  # 벽이면 밀 수 없음 
            return False

        c = chessboard[nx][ny]

        # 다른 기사가 있다면 연쇄적으로 밀 수 있는지 확인
        if c < 0 and c != -i:  # 자기 자신의 위치가 아니면서 다른 기사의 위치라면
            next_knight = -c

            if not can_push(next_knight, d):  # 재귀적으로 다른 기사도 밀 수 있는지 확인
                return False

    return True


for _ in range(Q):
    i, d = map(int, input().split())

    # 이미 죽은 기사라면 명령 무시
    if i not in knight:
        continue

    push_knight = []
    push_check = set()

    # 밀 수 없다면 명령 취소
    if not can_push(i, d):
        continue

    dx, dy = dirs[d]

    # 밀려야 하는 기사들의 기존 위치를 모두 지움
    for idx in push_knight:
        for x, y in knight[idx]:
            chessboard[x][y] = terrain[x][y]


    # 모든 기사들의 좌표를 이동
    for idx in push_knight:
        new_pos = []

        for x, y in knight[idx]:
            nx = x + dx
            ny = y + dy

            new_pos.append([nx, ny])

        knight[idx] = new_pos


    # 이동이 끝난 기사들을 체스판에 기록
    for idx in push_knight:
        for x, y in knight[idx]:
            chessboard[x][y] = -idx

    # 밀려난 기사들의 함정 피해 계산
    for idx in push_knight:

        # 명령받은 기사 본인은 피해 없음
        if idx == i:
            continue

        cnt = 0

        for x, y in knight[idx]:
            # 함정 여부는 terrain으로 확인
            if terrain[x][y] == 1:
                cnt += 1

        health[idx] -= cnt

        # 기사가 죽었다면 제거
        if health[idx] <= 0:

            for x, y in knight[idx]:
                chessboard[x][y] = terrain[x][y]

            del knight[idx]

        else:
            damaged[idx] += cnt

answer = 0

# 살아남은 기사들이 받은 대미지만 합산
for i in knight.keys():
    answer += damaged[i]

print(answer)