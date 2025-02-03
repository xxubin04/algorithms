# 이것이 코테다 p.115
# Ch.4 구현 
# 실전 문제 2 - 왕실의 나이트
# 걸린 시간: 10분 02초 
# 일시: 2025.02.03

location = list(input().rstrip())
x, y = int(location[1]), ord(location[0])
answer = 0

for i in [-1, 1]:  # 왼/오
  for j in [-1, 1]:  # 위/아래
    if 1 <= x + (i * 2) <= 8 and 97 <= y + (j) <= 104:
      answer += 1
      
for a in [-1, 1]:  # 위/아래
  for b in [-1, 1]:  # 왼/오
    if 1 <= x + a <= 8 and 97 <= y + (b * 2) <= 104:
      answer += 1

print(answer)
