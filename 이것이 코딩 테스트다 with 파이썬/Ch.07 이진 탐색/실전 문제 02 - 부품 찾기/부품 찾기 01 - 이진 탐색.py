input = open(0).readline

# 이진 탐색 함수
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return "yes"
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return "no"

n = int(input())  # 가게의 부품 개수 입력
array = sorted(list(map(int, input().split())))  # 가게의 부품 번호 입력
find_n = int(input())  # 확인 요청받은 부품의 개수 입력

# 확인 요청받은 부품 번호 입력 및 각각 확인
for target in list(map(int, input().split())):
    print(binary_search(array, target, 0, n-1), end=' ')
