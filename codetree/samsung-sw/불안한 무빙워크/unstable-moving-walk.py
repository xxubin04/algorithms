from collections import deque 

n, k = map(int, input().split())
q = [0] + list(map(int, input().split()))
first = 1  # 1번 칸의 번호
loc = deque([])  # 사람들의 위치(칸의 번호) 저장
occupied = set()  # 사람이 올라가 있는 실제 칸 번호 
qc = 0  # 안정성이 0인 칸의 개수 
cnt = 0  # 과정 반복 횟수 

while qc < k:
    cnt += 1

    # 1. 무빙워크 1칸 회전
    first -= 1
    if first == 0:
        first = 2 * n

    # 회전 후 n번 위치에 도착한 사람은 내림
    for _ in range(len(loc)):
        p, s = loc.popleft()

        if s + 1 == n:
            occupied.remove(p)
            continue
        
        loc.append((p, s + 1))

    # 2. 올라간 사람들 이동 
    for _ in range(len(loc)):
        p, s = loc.popleft()

        # 현재 칸 번호 기준으로 다음 칸 계산
        prior = p + 1

        if prior > 2 * n:
            prior = 1

        # 앞 칸에 사람이 있거나 안정성이 0이면 이동 불가
        if prior in occupied or q[prior] == 0:
            loc.append((p, s))
            continue 

        # 기존 칸에서 사람 뻄
        occupied.remove(p)

        # 앞 칸으로 이동했으므로 안정성 감소
        q[prior] -= 1

        if q[prior] == 0:
            qc += 1
        
        # 이동 후 n번 위치에 도착하면 내림 
        if s + 1 == n:
            continue 
        
        # n번 위치가 아니라면 새로운 위치 저장
        loc.append((prior, s + 1))
        occupied.add(prior)
        
    # 3. 1번 위치에 새로운 사람 올리기
    if first not in occupied and q[first] != 0:
        loc.append((first, 1))
        occupied.add(first)

        q[first] -= 1

        if q[first] == 0:
            qc += 1

print(cnt)