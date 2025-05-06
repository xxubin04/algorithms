input = open(0).readline
dir = [0, 1, 2, 3]  # 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
ans = 0

def now_clean(x, y, d):
    global ans
    if room[x][y] == 0:  # 현재 청소 X
        ans += 1
        room[x][y] = 2  # 청소 완료 표시
    around_clean(x, y, d)

def around_clean(x, y, d):
    for _ in range(4):
        d = (d + 3) % 4  # 반시계로 90도 회전
        if room[x + dx[d]][y + dy[d]] == 0:  # 앞의 빈칸이 청소 X
            now_clean(x + dx[d], y + dy[d], d)
            return
    back(x, y, d)

def back(x, y, d):
    bd = (d + 2) % 4  # 후진 방향
    if room[x + dx[bd]][y + dy[bd]] != 1:  # 벽이 아닌 경우 후진
        now_clean(x + dx[bd], y + dy[bd], d)

N, M = map(int, input().split())
initial_x, initial_y, initial_d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

now_clean(initial_x, initial_y, initial_d)
print(ans)
