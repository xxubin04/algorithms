from collections import deque
input = open(0).readline 

def BFS(c, x, y):
    global ans
    q = deque()
    q.append((c, x, y))
    while q:
        cnt, t, o = q.popleft()
        if t == o:
            ans.append(cnt)
            return 0
        if t * 2 <= o + 3:
            q.append((cnt+1, t*2, o+3))
        if t + 1 <= o:
            q.append((cnt+1, t+1, o))
    
for i in range(n := int(input())):
    ans = []
    tae, opp = map(int, input().split())
    BFS(0, tae, opp)
    print(min(ans))