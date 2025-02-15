# 이것이 코테다 p.201
# Ch.7 이진 탐색
# 실전 문제 3. 떡볶이 떡 만들기
# 걸린 시간: 8분 51초
# 일시: 2025.02.15

n, m = map(int, input().split())  # 떡의 개수, 요청한 떡의 길이
tteok_length = list(map(int, input().split()))  # 떡의 개별 높이들

def binary_search(tteok_length, start, end):
    while start < end:
        mid = (start + end) // 2
        tteok_sliced_length = 0
        for i in range(n):  # 잘린 떡의 총 길이 계산
            if tteok_length[i] - mid > 0:
                tteok_sliced_length += tteok_length[i] - mid
        if tteok_sliced_length == m:  # 잘린 떡의 총 길이가 요청한 떡의 길이와 같다면
            return mid
        elif tteok_sliced_length < m:
            end = mid-1
        else:
            start = mid+1

    return mid  # 잘린 떡의 총 길이가 요청한 떨의 길이와 맞아떨어질 수 없다면 높이의 최댓값 출력

print(binary_search(tteok_length, 0, max(tteok_length)))
