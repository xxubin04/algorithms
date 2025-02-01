# 이것이 코테다 p.96
# Ch.3 그리디
# 실전 문제 - 숫자 카드 게임  
# 걸린 시간: 05분 20초 
# 일시: 2025.01.31

N, M = map(int, input().split())  # 행, 열 입력
num = []  
min_num = 0

for i in range(N):  # 카드 정보 입력
  num.append(list(map(int, input().split())))

for j in range(N):  # 각 행을 탐색하면서
  if (m := min(num[j])) > min_num:  # 각 행의 최솟값이 앞선 행들의 최솟값보다 크면
    min_num = m  # 최솟값 갱신 
    
print(min_num)
    
