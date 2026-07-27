n, m = map(int, input().split())
packages = [[0 for _ in range(n+1)] for _ in range(n+1)]
info = {}

def fall(c, w):
    min_height = n + 1
    for col in range(c, c + w):
        top = n + 1
        for row in range(1, n + 1):
            if packages[row][col] != 0:
                top = row
                break

        min_height = min(min_height, top)

    return min_height

def draw_packages(k):
    r, c, h, w = info[k]
    for i in range(r, r+h):
        for j in range(c, c+w):
            packages[i][j] = k

def erase_packages(k):
    r, c, h, w = info[k]
    for i in range(r, r+h):
        for j in range(c, c+w):
            packages[i][j] = 0

def can_sub_left(r, c, h, w):
    for i in range(r, r+h):
        for j in range(1, c):
            if packages[i][j] != 0:
                return False
    
    return True 

def can_sub_right(r, c, h, w):
    for i in range(r, r+h):
        for j in range(c+w, n+1):
            if packages[i][j] != 0:
                return False
    
    return True

def apply_gravity():
    # 현재 더 아래에 있는 택배부터 다시 배치 
    package_order = sorted(info.keys(), key=lambda k: info[k][0] + info[k][2] - 1, reverse=True)

    # 격자 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            packages[i][j] = 0
    
    # 아래쪽 택배부터 다시 떨어뜨림
    for k in package_order:
        _, c, h, w = info[k]

        new_r = fall(c, w) - h
        info[k][0] = new_r

        draw_packages(k)

# 1. 택배 투입 
for _ in range(m):
    k, h, w, c = map(int, input().split())
    r = fall(c, w) - h  # 새로운 택배가 위치한 열의 최대 높이 (단, 좌표기 때문에 높이가 높을수록 높이가 낮음)
    info[k] = [r, c, h, w]  # [행, 열, 세, 가]
    draw_packages(k)

order = []  # 택배들 뽑는 순서

# 2. 왼/오 번갈아가며 택배 하차
for t in range(m):
    candidates = []

    # 짝수 번째 하차: 왼쪽
    if t % 2 == 0:
        for k in info:
            if can_sub_left(*info[k]):
                candidates.append(k)
    
    # 홀수 번째 하차: 오른쪽
    else:
        for k in info:
            if can_sub_right(*info[k]):
                candidates.append(k)
    
    # 하차 가능한 택배 중 번호가 가장 작은 택배 선택 
    target = min(candidates)

    erase_packages(target)
    del info[target]

    order.append(target)

    apply_gravity()

print(*order, sep="\n")