# 이것이 코테다 p.110
# Ch.4 구현 
# 예제 4-1. 상하좌우 
# 걸린 시간: 06분 13초 
# 일시: 2025.02.03

N = int(input())
shift = list(input().rstrip().split())
x, y = 1, 1

for s in shift:
  if s == 'R':  # 오른쪽 
    nx, ny = x, y+1
  elif s == "L":  # 왼쪽
    nx, ny = x, y-1
  elif s == "U":  # 위쪽
    nx, ny = x-1, y
  else:  # 아래쪽
    nx, ny = x+1, y

  if 0 < nx <= N and 0 < ny <= N:  # 공간 안일때만 
    x, y = nx, ny  # 좌표 적용 

print(x, y)
    
