def solution(n):
    used = 0

    while n > 1:
        if n%2 != 0:   # 홀수라면 1칸 점프
            used += 1
            n -= 1
        else:  # 짝수라면 (n/2)칸으로 순간이동
            n //= 2

    return used+1 if n == 1 else used
