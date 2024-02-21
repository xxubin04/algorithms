from itertools import combinations
input = open(0).readline 

num = int(input())

ans = 1000000000
density = [[0, 0] for _ in range(num)]

for j in range(num):
    density[j][0], density[j][1] = map(int, input().split())

for i in range(1, num+1):
    for j in combinations(density, i):
        sour = 1 
        bitter = 0 
        for k in j:
            sour *= k[0]
            bitter += k[1]
        ans = min(ans, abs(sour-bitter))

print(ans)