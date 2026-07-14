from collections import deque 

chairs = []
for _ in range(4):
    chairs.append(deque(map(int, input().strip())))

for _ in range(int(input())):
    num, dir = map(int, input().split())
    n = num - 1
    rotate_dir = [0] * 4
    rotate_dir[n] = dir

    # 왼쪽 확인
    for i in range(n, 0, -1):
        # 인접한 의자끼리 서로 다르다면
        if chairs[i][6] == chairs[i-1][2]:
            break
        
        rotate_dir[i-1] = -rotate_dir[i]
    
    # 오른쪽 확인
    for i in range(n, 3):
        if chairs[i][2] == chairs[i+1][6]:
            break 
        
        rotate_dir[i+1] = -rotate_dir[i]

    for i in range(4):
        if rotate_dir[i] == 1:
            chairs[i].rotate(1)
        elif rotate_dir[i] == -1:
            chairs[i].rotate(-1)        

    
print(chairs[0][0] + chairs[1][0] * 2 + chairs[2][0] * 4 + chairs[3][0] * 8)