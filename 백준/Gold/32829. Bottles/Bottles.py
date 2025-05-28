input = open(0).readline

runner, interval = map(int, input().split())
times_by_runner = [[] for _ in range(runner)]
cnt_list = [[] for _ in range(interval)]

for j in range(runner):
    time_interval = list(map(int, input().split()))
    for t in range(interval):
        if t == 0:
            times_by_runner[j].append((0, time_interval[0]))
        else:
            times_by_runner[j].append((times_by_runner[j][t-1][1], times_by_runner[j][t-1][1] + time_interval[t]))

for i in range(interval):
    runner_in_interval = []  # 각 구간에서의 러너의 시간 튜플 저장
    for r in range(runner):
        runner_in_interval.append(times_by_runner[r][i])

    events = []
    for start, end in runner_in_interval:
        events.append((start, 1))
        events.append((end, -1))

    events.sort()

    cnt = 0
    max_cnt = 0
    for _, c in events:
        cnt += c
        max_cnt = max(max_cnt, cnt)

    print(max_cnt, end=' ')