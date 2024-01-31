input = open(0).readline

cnt = int(input())
num = sorted([int(input()) for i in range(cnt)])
print(round(sum(num)/cnt))
print(int(num[cnt//2] if cnt%2 != 0 else sum(num[cnt//2-1:cnt//2+1])/2))
frq_list = {}
for j in num:
    if j in frq_list:
        frq_list[j] += 1
    else:
        frq_list[j] = 1
frq_list = sorted(frq_list.items(), reverse=True, key=lambda x:x[1])
frq_values = [k for k, v in frq_list if v == frq_list[0][1]]
print(frq_list[1][0] if len(frq_values) >= 2 else frq_list[0][0])
print(num[-1]-num[0])