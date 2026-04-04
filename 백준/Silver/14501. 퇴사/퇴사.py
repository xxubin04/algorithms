schedule = []

for _ in range(N :=  int(input())):
    schedule.append(tuple(map(int, input().split())))

max_profit = 0

def dfs(day, total):
    global max_profit
    max_profit = max(max_profit, total)

    if day >= N:
        return

    # 선택 1: 오늘 상담 안 잡기
    dfs(day+1, total)

    # 선택 2: 오늘 상담 잡기
    if day + schedule[day][0] <= N:
        dfs(day + schedule[day][0], total + schedule[day][1])

dfs(0, 0)
print(max_profit)