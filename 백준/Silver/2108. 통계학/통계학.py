from collections import Counter
input = open(0).readline

cnt = int(input())
num = sorted([int(input()) for i in range(cnt)])
print(round(sum(num)/cnt))
print(int(num[cnt//2] if cnt%2 != 0 else sum(num[cnt//2-1:cnt//2+1])/2))
frq = Counter(num)
frq_cnt = 0
for k, v in frq.items():
    if v == max(frq.values()): frq_cnt += 1
if frq_cnt >= 2:
    print(sorted(frq.items(), reverse=True, key=lambda x:x[1])[1][0])
else:
    print(sorted(frq.items(), reverse=True, key=lambda x:x[1])[0][0])
print(num[-1]-num[0])