# 이것이 코테다 p.220
# Ch.8 다이나믹 프로그래밍 
# 실전 문제 3. 개미 전사 
# 걸린 시간: 22분 2초
# 일시: 2025.02.16

n = int(input())
s = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * n

# Bottom-Up 방식으로 DP 진행
for i in range(n):  
    if i == 0:  # d[0] 초기화
        d[i] = s[i]
    elif i == 1:  # d[1] 초기화 
        d[i] = max(s[0], s[1])
    else:
        d[i] = max(s[i] + d[i-2], d[i-1])

print(d[n-1])
