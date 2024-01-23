input = open(0).readline

tree_num = int(input())
time = sorted(list(map(int, input().split())), reverse=True)
time_growth = list(idx + t for idx, t in enumerate(time, start=1))
print(max(time_growth)+1)