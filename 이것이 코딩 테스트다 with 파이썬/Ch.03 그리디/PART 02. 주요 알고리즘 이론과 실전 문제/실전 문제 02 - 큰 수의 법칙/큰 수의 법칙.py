# 이것이 코테다 p.92
# Ch.3 그리디
# 실전 문제 - 큰 수의 법칙 
# 걸린 시간: 03분 11초

# N: 입력받는 수들의 개수, M: 더하는 횟수, K: 최대 연속가능 횟수 
N, M, K = map(int, input().split())  
# 입력받은 수들을 내림차순으로 정렬하여 저장 
numbers = sorted(list(map(int, input().split())), reverse=True)

cnt = 0  # 총 연속 횟수
total = 0  # 수들을 더한 합계 
for i in range(M):
  if cnt != K:  # 연속 횟수가 K가 아니라면 
    total += numbers[0]  # 가장 큰 수를 더함
    cnt += 1  # 연속 횟수 증가 
  else:  # 연속 횟수가 K라면 
    total += numbers[1]  # 두 번째로 큰 수를 더함 
    cnt = 0  # 연속 횟수 0으로 초기화
    
print(total)
