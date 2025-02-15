n, m = map(int, input().split())  # 떡의 개수, 요청한 떡의 길이
tteok_length = list(map(int, input().split()))  # 떡의 개별 높이들

start, end = 0, max(tteok_length)
result = 0

while start < end:
    tteok_sliced_length = 0
    mid = (start + end) // 2
    for i in range(n):  # 잘린 떡의 총 길이 계산
        if tteok_length[i] > mid:
            tteok_sliced_length += tteok_length[i] - mid
    if tteok_sliced_length < m:
        end = mid - 1
    else:  # 요청한 떡의 길이보다 잘린 떡의 총 길이가 크거나 같을 때 
        result = mid  # 조건을 만족하였으므로 result에 기록 
        start = mid+1

print(result)
