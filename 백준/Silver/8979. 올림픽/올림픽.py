input = open(0).readline

medal = {}
nation_num, wanna_rank = map(int, input().split())

for _ in range(nation_num):
    nation, gold, silver, bronze = map(int, input().split())
    medal[nation] = [gold, silver, bronze]

line = sorted(medal.values(), key=lambda x: (x[0], x[1], x[2]), reverse=True)
print(line.index(medal[wanna_rank])+1)