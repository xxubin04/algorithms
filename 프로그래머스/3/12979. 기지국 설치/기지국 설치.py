# def solution(n, stations, w):
#     answer = 0
#     reach_check = [1] + ([0] * n)
    
#     # 기존의 기지국의 전파 확인
#     for s in stations:
#         reach_check[s] = 1
#         for left in range(s-w, s):
#             if left >= 0:
#                 reach_check[left] = 1
#         for right in range(s+1, s+w+1):
#             if right <= n:
#                 reach_check[right] = 1
    
#     # 추가 증설해야 하는 기지국 위치 설정
#     for idx in range(1, n+1):
#         if reach_check[idx] == 1:
#             continue 
        
#         for i in range(idx, idx+2*w+1):
#             if i <= n:
#                 reach_check[i] = 1

#         answer += 1
    
#     return answer


def solution(n, stations, w):
    start = 1
    block = []  # 전파되지 않는 아파트들 개수 묶음 
    answer = 0
    
    stations.sort()
    
    for s in stations:
        l = s - w - 1  # 왼쪽에서 전파 안되는 시점 시작
        r = s + w + 1   # 오른쪽에서 전파 안되는 시점 시작
    
        # 왼쪽 확인
        if start <= l:
            block.append(l - start + 1)

        start = r
    
    if (n-r+1) > 0:
        block.append(n-r+1)
    
    for b in block:
        answer += ((b - 1) // (2 * w + 1) + 1)
    
    return answer
        