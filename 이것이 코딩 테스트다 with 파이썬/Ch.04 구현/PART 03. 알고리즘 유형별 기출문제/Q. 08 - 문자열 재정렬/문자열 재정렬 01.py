# 이것이 코테다 p.322
# Ch.4 구현 
# 기출 문제 - 08. 문자열 재정렬
# 걸린 시간: 02분 50초 
# 일시: 2025.02.04

S = sorted(list(input()))
total = 0
answer = ""

for s in S:
  if s.isdigit():
    total += int(s)
  else:
    answer += s

print(answer + str(total))
