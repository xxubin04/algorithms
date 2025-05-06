from math import ceil

place = int(input())
candidates = list(map(int, input().split()))
sup_info = list(map(int, input().split()))

cnt = place

if len(sup_info) == 2:
    sub = sup_info[1]

sup = sup_info[0]

for i in range(place):
    candidates[i] -= sup
    if candidates[i] < 0:
        continue
    cnt += ceil(candidates[i] / sub)

print(cnt)
