input = open(0).readline

num = int(input())
room = sorted([list(map(int, input().split())) for _ in range(num)])
room.sort(key=lambda x: x[1])

time, cnt = 0, 0

for start, end in room:
    if start >= time:
        time = end
        cnt += 1

print(cnt)