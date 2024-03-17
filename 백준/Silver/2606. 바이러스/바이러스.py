input = open(0).readline 

computer_num = int(input())
connection = [[] for _ in range(computer_num+1)]

visited = [0 for _ in range(computer_num+1)]

def dfs(x, y, z):
    if visited[x] == 0:
        visited[x] = 1 
        for j in connection[x]:
            dfs(j, cnt, visited)
    
for i in range(n := int(input())):
    a, b = map(int, input().split())
    connection[a].append(b); connection[b].append(a)

cnt = 0
dfs(1, cnt, visited)

print(sum(visited)-1)