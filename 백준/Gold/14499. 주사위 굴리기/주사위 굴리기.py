import sys

dice = [0] * 6
map_info = []
row, col, x, y, cmd = map(int, sys.stdin.readline().split())

for _ in range(row):
    map_info.append(list(map(int, sys.stdin.readline().split())))

def check_in_bound(x, y):
    if 0 <= x < row and 0 <= y < col:
        return True

for dir in (cmd_info := list(map(int, sys.stdin.readline().split()))):
    if dir == 1:  # 동쪽
        y += 1
        if check_in_bound(x, y):
            temp = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = dice[2]
            dice[2] = temp
            print(dice[0])
            if map_info[x][y] == 0:
                map_info[x][y] = dice[5]
            else:
                dice[5] = map_info[x][y]
                map_info[x][y] = 0

        else:
            y -= 1
            continue
    elif dir == 2:  # 서쪽
        y -= 1
        if check_in_bound(x, y):
            temp = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = dice[3]
            dice[3] = temp
            print(dice[0])
            if map_info[x][y] == 0:
                map_info[x][y] = dice[5]
            else:
                dice[5] = map_info[x][y]
                map_info[x][y] = 0
        else:
            y += 1
            continue
    elif dir == 3:  # 북쪽
        x -= 1
        if check_in_bound(x, y):
            temp = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = dice[1]
            dice[1] = temp
            print(dice[0])
            if map_info[x][y] == 0:
                map_info[x][y] = dice[5]
            else:
                dice[5] = map_info[x][y]
                map_info[x][y] = 0
        else:
            x += 1
            continue
    else:  # 남쪽
        x += 1
        if check_in_bound(x, y):
            temp = dice[0]
            dice[0] = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[4]
            dice[4] = temp
            print(dice[0])
            if map_info[x][y] == 0:
                map_info[x][y] = dice[5]
            else:
                dice[5] = map_info[x][y]
                map_info[x][y] = 0
        else:
            x -= 1
            continue
