answer = 0
cow = []
m, s, c = map(int, input().split())

for i in range(c):
    cow.append(int(input()))

cow.sort()
dist = []

for i in range(1, len(cow)):
    dist.append(cow[i] - cow[i-1] -1 )

dist.sort(reverse = True)
answer = cow[-1] - cow[0] + 1

for i in range(m-1):
    answer -=dist[i]

print(answer)
