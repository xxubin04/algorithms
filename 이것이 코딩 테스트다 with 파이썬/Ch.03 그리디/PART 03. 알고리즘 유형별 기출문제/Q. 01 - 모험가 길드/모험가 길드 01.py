# 이것이 코테다 p.311
# Ch.11 그리디
# 기출 문제 - 01. 모험가 길드
# 걸린 시간: 04분 51초 
# 일시: 2025.02.01

N = int(input())
# 내림차순으로 공포도 정렬
scary = sorted(list(map(int, input().split())), reverse=True)

cnt = 0  # 모험을 떠나는 그룹 수

while scary:  # 남은 공포도(사람)가 있다면
  i = scary[0]  # 남은 사람들 중 가장 높은 공포도
  scary = scary[i:]  # 공포도가 높은 사람들 i명 제거(집단 생성)
  cnt += 1  # 집단 수 1 증가
  
print(cnt)
