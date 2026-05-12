from math import ceil

rest = int(input())
cust = list(map(int, input().split()))
ldr, mbr = map(int, input().split())

ans = rest
for i in range(rest):
    if (c := cust[i]-ldr) > 0:
        ans += ceil(c/mbr)

print(ans)