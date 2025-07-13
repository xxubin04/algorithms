import sys

width, length = map(int, sys.stdin.readline().rstrip().split())  # 가로, 세로
x_list, y_list = [0, width], [0, length]
max_area = 0

for _ in range(int(sys.stdin.readline().rstrip())):
    x_cut_YN, num = map(int, sys.stdin.readline().rstrip().split())
    if x_cut_YN and not num in x_list:  # 가로라면
        x_list.append(num)
    elif not x_cut_YN and not num in y_list:  # 세로라면
        y_list.append(num)
x_list.sort()
y_list.sort()

for i in range(1, len(x_list)):
    for j in range(1, len(y_list)):
        if (area := (x_list[i] - x_list[i-1]) * (y_list[j] - y_list[j-1])) > max_area:
            max_area = area

print(max_area)