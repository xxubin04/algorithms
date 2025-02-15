# 이것이 코테다 p.113
# Ch.4 구현 
# 예제 4-2. 시각 
# 걸린 시간: 10분 02초 
# 일시: 2025.02.03

N = int(input())
hour_cnt = 0  # '시(hour)'에 3이 들어가는 경우의 수 

for n in range(N+1):
  if n in [3, 13, 23]:
    hour_cnt += 1

answer = (N+1) * 3600 - ((N+1) - hour_cnt) * 45 *45

print(answer)
