# 이것이 코테다 p.182
# Ch.6 정렬 
# 실전 문제 4. 두 배열의 원소 교체 
# 걸린 시간: 2분 56초
# 일시: 2025.02.14

n, k = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

for i in range(k):
    if A[i] < B[n-i-1]:
        A[i], B[n-i-1] = B[n-i-1], A[i]
    else:
        break

print(sum(A))
