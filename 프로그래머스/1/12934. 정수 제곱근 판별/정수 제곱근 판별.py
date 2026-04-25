def binary_search(target, data):
    start, end = 0, target
    
    while start <= end:
        mid = (start + end) // 2
        
        if mid ** 2 == target:  # 제곱수라면
            return (mid + 1) ** 2
        elif mid ** 2 > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1
        
    
def solution(n):
    return binary_search(n, range(1, n+1))
        