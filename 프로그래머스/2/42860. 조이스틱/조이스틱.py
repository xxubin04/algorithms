def solution(name):
    answer = 0
    n = len(name)

    # 1. 위/아래 조작 횟수
    for c in name:
        up = ord(c) - ord('A')
        down = ord('Z') - ord(c) + 1

        answer += min(up, down)

    # 2. 좌/우 이동 횟수
    move = n - 1

    for i in range(n):
        next_idx = i + 1

        # 연속된 A 구간 찾기
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 오른쪽으로 갔다가 되돌아오기
        case1 = i * 2 + (n - next_idx)

        # 왼쪽 방향을 먼저 갔다가 되돌아오기
        case2 = (n - next_idx) * 2 + i

        move = min(move, case1, case2)

    return answer + move