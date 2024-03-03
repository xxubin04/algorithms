input = open(0).readline

rank = []
total = 0
for i in range(n := int(input())):
    rank.append(int(input()))
    
rank.sort()
for j in range(n):
    total += abs(rank[j] - (j+1))
    
print(total)