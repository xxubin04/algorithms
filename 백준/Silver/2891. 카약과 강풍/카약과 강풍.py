import sys

n, s, r = map(int, sys.stdin.readline().split())
team = [1] * n  

for i in list(map(int, sys.stdin.readline().split())):
    team[i-1] -= 1  
for i in list(map(int, sys.stdin.readline().split())):
    team[i-1] += 1  
    
cannot_start = 0

for j in range(n):
    if team[j] == 0:
        if j > 0 and team[j-1] == 2:
            team[j-1] -= 1
            team[j] += 1
        elif j < n-1 and team[j+1] == 2:
            team[j+1] -= 1
            team[j] += 1
        else:
            cannot_start += 1

print(cannot_start)