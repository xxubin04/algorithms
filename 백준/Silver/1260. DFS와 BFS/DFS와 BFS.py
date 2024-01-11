from collections import deque
import copy
import sys
sys.setrecursionlimit(10**6)

input = open(0).readline

num, line, start = map(int, input().split())

node = [[] for _ in range(num+1)]
for i in range(line):
    A, B = map(int, input().split())
    node[A].append(B)
    node[B].append(A)

for j in range(num+1):
    node[j].sort()

visited_DFS = [0 for _ in range(num+1)]
visited_BFS = [0 for _ in range(num+1)]
visited_BFS[start] = 1
ans_DFS = []
ans_BFS = [start]
proD = []
proB = deque([start])

def DFS(x):
    if visited_DFS[x] == 0:
        visited_DFS[x] = 1
        ans_DFS.append(x)
        proD.append(node[x])
        for d in node[x]:
            DFS(d)

def BFS(x):
    while proB:
        proB.popleft()
        for c in node[x]:
            if visited_BFS[c] == 0:
                proB.append(c)
                ans_BFS.append(c)
            visited_BFS[c] = 1
        for k in copy.deepcopy(proB):
            BFS(k)

DFS(start)
BFS(start)

for a in ans_DFS:
    print(a, end=' ')
print("\n", end="")
for b in ans_BFS:
    print(b, end=' ')