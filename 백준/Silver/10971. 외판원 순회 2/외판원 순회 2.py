import sys
sys.setrecursionlimit(10**6)

w = []

def tsp(i, visited, cost):
    min_cost = float('inf')

    if all(visited):
        if w[i][0] != 0:
            return cost + w[i][0]
        else:
            return float('inf')

    for j in range(1, n):
        if visited[j] == 0 and w[i][j] != 0:
            visited[j] = 1
            min_cost = min(min_cost, tsp(j, visited, cost + w[i][j]))
            visited[j] = 0

    return min_cost

for _ in range(n := int(sys.stdin.readline().strip())):
    w.append(list(map(int, sys.stdin.readline().strip().split())))

visited = [1] + [0] * (n-1)

print(tsp(0, visited, 0))