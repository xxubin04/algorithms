# 이것이 코테다 p.113
# Ch.4 구현 
# 예제 4-2. 시각 
# 걸린 시간: 2분?
# 일시: 2025.02.03

N = int(input())
answer = 0

for h in range(N+1):
  for m in range(60):
    for s in range(60):
      if str(h).find('3') + str(m).find('3') + str(s).find('3') != -3:
        answer += 1

print(answer)
