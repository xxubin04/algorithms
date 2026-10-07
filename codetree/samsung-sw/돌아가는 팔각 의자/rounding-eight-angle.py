import sys
from collections import deque 

input = sys.stdin.readline

chairs = [deque(map(int, input().strip())) for _ in range(4)]

for _ in range(K := int(input())):
    n, d = map(int, input().strip().split())
    n -= 1   # 1-based

    rotate = [0, 0, 0, 0]  # 각 의자가 회전하는 방향 
    rotate[n] = d

    # 왼쪽 방향으로 확인
    for i in range(n, 0, -1):
        if chairs[i-1][2] != chairs[i][6]:
            rotate[i-1] = -rotate[i]
        else:
            break
    
    # 오른쪽 방향으로 확인
    for i in range(n, 3):
        if chairs[i][2] != chairs[i+1][6]:
            rotate[i+1] = -rotate[i]
        else:
            break
    
    for i in range(4):
        if rotate[i] == 1:  # 시계 방향
            chairs[i].rotate(1)
        elif rotate[i] == -1:  # 반시계 방향
            chairs[i].rotate(-1)
    
    answer = 0
    
    for i in range(4):
        if chairs[i][0] == 1:  # 남쪽지방 사람이라면
            answer += 2 ** i 
    
print(answer)