# 이것이 코테다 p.178
# Ch.6 정렬
# 실전 문제 2. 위에서 아래로
# 걸린 시간: 47초
# 일시: 2025.02.10

array = []

for _ in range(n := int(input())):
    array.append(int(input()))

for i in sorted(array, reverse=True):
    print(i, end=' ')
