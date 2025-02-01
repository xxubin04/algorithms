# 이것이 코테다 p.313
# Ch.11 그리디
# 기출 문제 - 03. 문자열 뒤집기
# 걸린 시간: 04분 12초 
# 일시: 2025.02.01

import math as m

S = list(map(int, input()))
prior = S[0]
cnt = 0  # 직전의 수와 다른 경우 세기

for s in range(1, len(S)):
  if S[s] != prior:  # 직전의 수와 다르다면 cnt 1 증가
    cnt += 1  
    prior = S[s]

print(m.ceil(cnt/2))  # 직전의 수와 다른 수를 2로 나누고 올림 = 최소 횟수
