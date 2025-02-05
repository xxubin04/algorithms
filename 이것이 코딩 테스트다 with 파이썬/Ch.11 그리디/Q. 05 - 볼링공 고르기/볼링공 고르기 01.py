# 이것이 코테다 p.315
# Ch.11 그리디
# 기출 문제 - 05. 볼링공 고르기
# 걸린 시간: 03분 20초 
# 일시: 2025.02.01

N, M = map(int, input().split())

weights = sorted(list(map(int, input().split())))
cnt = 0  # 무게가 다른 볼링공 조합 개수

for i in range(N):
  for j in range(i, N):
    if weights[i] != weights[j]:  # 무게가 다른 경우에만 +1
      cnt += 1

print(cnt)
