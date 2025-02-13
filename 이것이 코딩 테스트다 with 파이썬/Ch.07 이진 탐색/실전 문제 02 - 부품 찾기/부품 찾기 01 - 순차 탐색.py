# 이것이 코테다 p.197
# Ch.7 이진 탐색
# 실전 문제 2. 부품 찾기
# 걸린 시간: 2분 29초
# 일시: 2025.02.13

input = open(0).readline

n = int(input())
array = list(map(int, input().split()))
find_n = int(input())
find_array = list(map(int, input().split()))

for i in find_array:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')
