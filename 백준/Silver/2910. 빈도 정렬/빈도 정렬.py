input = open(0).readline

N, C = map(int, input().split())

num_arr = list(map(int, input().split()))
cnt_arr = {}

for n in num_arr:
    if not n in cnt_arr:
        cnt_arr[n] = 1
    else:
        cnt_arr[n] += 1

cnt_arr = sorted(cnt_arr.items(), key=lambda x: x[1], reverse=True)

for key in cnt_arr:
    for j in range(key[1]):
        print(key[0], end=" ")