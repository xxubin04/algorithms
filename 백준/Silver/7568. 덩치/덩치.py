input = open(0).readline

info = []
rank = {}
for n in range(N := int(input())):
    info.append(list(map(int, input().split())))
    rank[n] = 0

for i in range(N):
    for j in range(i+1, N):
        if info[i][0] > info[j][0] and info[i][1] > info[j][1]:
            rank[j] += 1
        elif info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            rank[i] += 1

rank_sort = sorted(rank.items(), key=lambda x: x[1])

for i in range(N):
    print(rank[i]+1, end=" ")