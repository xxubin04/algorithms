# 이것이 코테다 p.99
# Ch.3 그리디
# 실전 문제 - 1이 될 때까지  
# 걸린 시간: 01분 55초 
# 일시: 2024.01.31

N, K = map(int, input().split())
cnt = 0  # 과정 수행 횟수 

while N > 1:
  if N % K == 0:  # K로 나누어 떨어진다면
    N /= K  # K로 나누기 
  else:  # K로 나누어 떨어지지 않는다면 
    N -= 1  # 1 빼기
  cnt += 1

print(cnt)
