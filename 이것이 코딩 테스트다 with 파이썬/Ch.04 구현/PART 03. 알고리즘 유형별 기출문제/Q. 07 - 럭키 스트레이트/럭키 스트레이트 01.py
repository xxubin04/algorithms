# 이것이 코테다 p.321
# Ch.4 구현 
# 기출 문제 - 07. 럭키 스트레이트
# 걸린 시간: 02분 23초 
# 일시: 2025.02.04

N = list(map(int, input()))

if sum(N[:len(N)//2]) == sum(N[len(N)//2:]):
  print("LUCKY")
else:
  print("READY")
