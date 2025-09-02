import sys

n = sys.stdin.readline().strip()
cnt = [0] * 10 

for digit in n:
    d = int(digit)
    if d == 6 or d == 9:
        cnt[6] += 1 
    else:
        cnt[d] += 1

cnt[6] = (cnt[6] + 1) // 2

print(max(cnt))  
