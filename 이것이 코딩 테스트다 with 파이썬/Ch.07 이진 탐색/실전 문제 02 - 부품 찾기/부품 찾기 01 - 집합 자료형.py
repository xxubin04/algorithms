# 특정한 수가 한 번이라도 등장했는지 검사하기 위해
# 집합 자료형 사용

input = open(0).readline

n = int(input())
array = set(map(int, input().split()))
find_n = int(input())
find_array = list(map(int, input().split()))

for i in find_array:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')
