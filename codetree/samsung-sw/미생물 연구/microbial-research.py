from collections import deque

N, Q = map(int, input().split())  # N: 좌표 크기, Q: 실험 횟수
micro_info = {}  # 미생물 무리마다의 정보 저장하는 딕셔너리
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

## [1] 미생물 투입
# 1. 미생물 투입 + 덮어씌워지는 기존의 미생물 번호 저장
def input_micro(r1, c1, r2, c2, num):
    for i in range(r1, r2):
        for j in range(c1, c2):
            # 이미 다른 미생물이 있다면 + 아직 리스트에 저장 안되어있다면 -> 해당 번호를 리스트에 저장
            if (dm := graph[i][j]) != 0:
                # 덮이는 모든 칸만큼 넓이 감소
                micro_info[dm][4] -= 1

                # 검사할 미생물 번호는 한 번만 저장
                if dm not in disappear_num:
                    disappear_num.append(dm)

            graph[i][j] = num  # 미생물의 번호로 좌표 갱신

    # 2개 이상으로 나누어짐 미생물 번호들은 전부 제거
    divided_micro = check_divided()  # 2개 이상으로 나누어지는 미생물 번호 저장

    for dm in divided_micro:
        del micro_info[dm]  # 미생물 정보 리스트에서 해당 미생물을 완전 제거

        # graph에서도 완전히 제거
        for i in range(N):
            for j in range(N):
                if graph[i][j] == dm:
                    graph[i][j] = 0


# 2. 2개 이상으로 나누어지는지 확인
def check_divided():
    # 새로운 미생물 때문에 덮어씌워진 미생물들이 2개 이상으로 나뉘어지는지 확인
    # 덮어씌워진 미생물마다 BFS로 한 번에 넓이만큼 순회 안되는지 확인
    divided_micro = []  # 완전 제거해야 할 미생물 번호 저장

    for dm in disappear_num:

        # 현재 graph에서 dm이 남아있는 좌표 하나 찾기
        start = None

        for i in range(N):
            for j in range(N):
                if graph[i][j] == dm:
                    start = (i, j)
                    break

            if start:
                break

        # 미생물이 완전히 덮여서 하나도 남지 않은 경우
        if start is None:
            divided_micro.append(dm)
            continue

        mx, my = start

        q = deque([(mx, my)])
        visited = [[0] * N for _ in range(N)]
        visited[mx][my] = 1

        size = 0

        while q:
            x, y = q.popleft()
            size += 1

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if (0 <= nx < N and 0 <= ny < N and graph[nx][ny] == dm and not visited[nx][ny]):
                    visited[nx][ny] = 1
                    q.append((nx, ny))

        # 한 번의 BFS로 전체 영역을 방문하지 못함
        # 2개 이상으로 분리됨
        if size != micro_info[dm][4]:
            divided_micro.append(dm)

    return divided_micro


## [2] 배양 용기 이동
# 4. 미생물마다 영억의 크기 내림차순으로 정렬
def sort_by_size(micro_list):
    return sorted(micro_list, key=lambda x: (-x[4], x[5]))  # 크기가 큰 순서대로, 먼저 투입된 순서대로


# 6. 조건 만족 + (x, y) 작은 순서대로
# [조건] 1. 기존 용기에서의 형태 유지
#       2. 범위 안
#       3. 다른 미생물과 겹치지 않게
def loc_with_condition():

    for micro in micro_list:
        r1, c1, r2, c2, extent, num = micro
        # r1, c1, r2, c2, 넓이, 미생물 번호

        # 현재 graph에서 해당 미생물의 좌표들을 저장
        positions = []

        for i in range(N):
            for j in range(N):
                if graph[i][j] == num:
                    positions.append((i, j))

        # 존재하지 않는 미생물이면 넘어감
        if not positions:
            continue

        # 미생물의 가장 작은 x, y 좌표
        min_x = min(x for x, y in positions)
        min_y = min(y for x, y in positions)

        # 미생물의 모양을 상대좌표로 변환
        relative_pos = []
        for x, y in positions:
            relative_pos.append((x - min_x, y - min_y))

        # 미생물 모양의 가로/세로 범위
        height = max(x for x, y in relative_pos) + 1
        width = max(y for x, y in relative_pos) + 1

        located = False  # 배치 여부

        # (x, y)가 작은 순서대로 확인
        for x in range(N - height + 1):
            for y in range(N - width + 1):

                possible = True

                # 현재 위치에 미생물 모양 전체를 놓을 수 있는지 확인
                for dx, dy in relative_pos:
                    nx, ny = x + dx, y + dy

                    # 이미 다른 미생물이 있으면 배치 불가능
                    if move_graph[nx][ny] != 0:
                        possible = False
                        break

                # 조건을 모두 만족하면 실제로 배치
                if possible:
                    for dx, dy in relative_pos:
                        nx, ny = x + dx, y + dy
                        move_graph[nx][ny] = num

                    located = True
                    break

            if located:
                break

        # 어느 위치에도 놓을 수 없다면 제거
        if not located:
            cannot_locate(num)


# 7. 어느 곳에도 무리를 둘 수 없다면
def cannot_locate(num):
    # 다음 실험부터 존재하지 않는 미생물로 처리
    if num in micro_info:
        del micro_info[num]


## [3] 실험 결과 기록
# 8. 인접한 무리끼리의 쌍 저장
def near_pair():
    pair_set = set()

    # 오른쪽, 위쪽(배열상 아래쪽)만 확인하면
    # 같은 쌍을 반복 확인하지 않아도 됨
    check_dirs = [(0, 1), (1, 0)]

    for x in range(N):
        for y in range(N):

            # 빈 공간이면 넘어감
            if move_graph[x][y] == 0:
                continue

            num1 = move_graph[x][y]

            for dx, dy in check_dirs:
                nx, ny = x + dx, y + dy

                # 범위 안인지 확인
                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                num2 = move_graph[nx][ny]

                # 빈 공간이거나 같은 미생물이면 인접쌍이 아님
                if num2 == 0 or num1 == num2:
                    continue

                # 같은 쌍을 중복 저장하지 않도록 작은 번호가 앞으로 오게 저장
                pair = tuple(sorted((num1, num2)))
                pair_set.add(pair)

    return pair_set


# 9. 인접쌍끼리의 결과 계산
def cal_result():
    pair_set = near_pair()

    # 현재 배양 용기에서 각 미생물의 넓이 계산
    area = {}

    for x in range(N):
        for y in range(N):
            num = move_graph[x][y]

            if num != 0:
                area[num] = area.get(num, 0) + 1

    result = 0

    # 인접한 두 미생물의 넓이 곱을 더함
    for num1, num2 in pair_set:
        result += area[num1] * area[num2]

    return result


## [메인 함수]
move_graph = [[0] * N for _ in range(N)]

for num in range(1, Q + 1):

    # 미생물 좌표, 넓이 저장
    r1, c1, r2, c2 = map(int, input().split())  # r1, c1, r2, c2의 좌표 입력
    extent = (r2 - r1) * (c2 - c1)  # 미생물의 크기
    micro_info[num] = [r1, c1, r2, c2, extent]  # r1, c1, r2, c2, 넓이 저장

    graph = [row[:] for row in move_graph]  # 이전 실험에서 이동한 좌표를 복사
    move_graph = [[0] * N for _ in range(N)]  # N x N 크기의 격자 생성 (이동할 격자)

    ## [1] 미생물 투입
    disappear_num = []  # 없어지는 미생물 번호 저장

    input_micro(r1, c1, r2, c2, num)

    ## [2] 배양 용기 이동
    micro_list = []  # 미생물의 정보를 리스트에 저장

    for idx, info in micro_info.items():
        micro_list.append(info + [idx])  # [r1, c1, r2, c2, 넓이, 번호]로 저장

    micro_list = sort_by_size(
        micro_list
    )  # 크기 내림차순 + 투입 순서대로 정렬

    # 조건에 맞게 새로운 배양 용기에 이동
    loc_with_condition()

    ## [3] 실험 결과 기록
    result = cal_result()

    print(result)