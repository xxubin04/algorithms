# 이것이 코테다 p.312
# Ch.11 그리디
# 기출 문제 - 02. 곱하기 혹은 더하기
# 걸린 시간: 05분 54초 
# 일시: 2024.02.01

S = list(map(int, input()))
total = 0  # 연산결과
first = S[0] 

for n in range(1, len(S)):
  second = S[n]
  if first == 0 or second == 0:  # 피연산자 2개 중 하나라도 0이라면
    total = (first + second)  # 더하기
    first = total
  else:  # 피연산자 2개 모두 0이 아니라면
    total = (first * second)  # 곱하기
    first = total

print(total)
