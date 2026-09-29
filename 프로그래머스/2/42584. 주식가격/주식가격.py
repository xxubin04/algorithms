def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    for i in range(n):
        # 현재 가격이 이전 가격보다 떨어졌다면
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
            
        stack.append(i)
    
    # 끝까지 가격이 떨어지지 않은 경우
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
    
    return answer