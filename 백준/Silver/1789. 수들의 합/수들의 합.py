n = int(input())
total = 0
i = 1
cnt = 0

def fun(total, n, i, cnt):
    while total < n:
        total += i
        i += 1
        cnt += 1
        if total > n:
            return cnt-1

    return cnt

print(fun(total, n, i, cnt))