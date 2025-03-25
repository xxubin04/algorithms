n, k = map(int, input().split())
values = []

for _ in range(n):
    values.append(int(input()))

values.sort(reverse = True)
cnt = 0

for c in values:
    if c <= k:
        cnt += k // c 
        k %= c 

print(cnt)