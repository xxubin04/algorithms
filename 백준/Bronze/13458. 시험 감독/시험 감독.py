import math

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    total = N  # 총감독관은 각 시험장마다 무조건 1명씩은 있어야 함

    for a in A:
        remain = a - B
        if remain > 0:
            total += math.ceil(remain / C)

    print(total)

solution()