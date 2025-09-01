import sys

score = 0
cogwheels = []
for _ in range(4):
    cogwheels.append(list(map(int, sys.stdin.readline().rstrip())))

for _ in range(int(sys.stdin.readline())):
    wheel, dir = map(int, sys.stdin.readline().split())

    rotate_dir = [0] * 4
    rotate_dir[wheel - 1] = dir

    # 기준 톱니바퀴의 왼쪽
    for i in range(wheel-1, 0, -1):
        if cogwheels[i][6] != cogwheels[i-1][2]:
            rotate_dir[i-1] = -rotate_dir[i]
        else:
            break

    # 기준 톱니바퀴의 오른쪽
    for i in range(wheel-1, 3):
        if cogwheels[i][2] != cogwheels[i+1][6]:
            rotate_dir[i+1] = -rotate_dir[i]
        else:
            break

    for i in range(4):
        if rotate_dir[i] == 1:
            cogwheels[i] = [cogwheels[i][-1]] + cogwheels[i][:-1]
        elif rotate_dir[i] == -1:
            cogwheels[i] = cogwheels[i][1:] + [cogwheels[i][0]]

for i in range(4):
    if cogwheels[i][0] == 1:
        if i == 0:      score += 1
        elif i == 1:    score += 2
        elif i == 2:    score += 4
        elif i == 3:    score += 8

print(score)