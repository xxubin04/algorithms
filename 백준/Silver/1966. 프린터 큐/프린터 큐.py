from collections import deque 
input = open(0).readline

for _ in range(int(input())):
    N, M = map(int, input().split())  # 문서의 개수, 궁금한 문서의 위치
    nums = list(map(int, input().split()))  # 중요도 입력된 리스트
    q = deque([])  # (순서, 중요도)로 입력된 리스트 

    for idx in range(len(nums)):
        q.append((idx, nums[idx]))
    
    seq = 1  # 몇 번째로 인쇄되는지 
    while q:
        m = max(x[1] for x in q) if q else -1
        idx, sig = q.popleft()
        if idx == M and sig >= m:  # 현재의 문서가 M번이면서, 중요도가 제일 클 때
            print(seq)
            break
        elif sig < m:  # 현재의 문서보다 중요도가 더 큰 문서가 있다면 
            q.append((idx, sig))
        else:  # 현재의 문서보다 중요도가 더 큰 문서가 없거나 / M번 문서이면서 M번 문서보다 중요도가 더 큰 문서가 있을 때
            seq += 1