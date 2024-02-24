from collections import deque
input = open(0).readline

people_num = int(input())
A, B = map(int, input().split())
relation_num = int(input())
relationship = [[0] for _ in range(people_num + 1)]

for i in range(relation_num):
    a, b = map(int, input().split())
    if relationship[a] == [0]:
        relationship[a] = [b]
    else:
        relationship[a].append(b)
    
    if relationship[b] == [0]:
        relationship[b] = [a]
    else:
        relationship[b].append(a)

visited = [0 for _ in range(people_num + 1)]

def chon(r, c, p):
    global ans, check
    q = deque()
    q.append((r, c, p))
    while q:
        relation, cnt, person = q.popleft()
        if visited[person] == 0:
            visited[person] = 1
            cnt += 1
            for j in relation[person]:
                if j == A:
                    ans.append(cnt)
                    return ans
                q.append((relation, cnt, j))
                
ans = []       
cnt = 0
answer = chon(relationship, cnt, B)
print(min(answer) if answer else -1)