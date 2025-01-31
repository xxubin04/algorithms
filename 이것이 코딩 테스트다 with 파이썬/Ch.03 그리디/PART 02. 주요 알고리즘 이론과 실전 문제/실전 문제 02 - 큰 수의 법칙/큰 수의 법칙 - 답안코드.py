N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

# 가장 큰 수가 더해지는 횟수
count = M // (K+1) * K  
count += M % (K+1)  

result = 0
result += count * first
result += (M - count) * second  # 두 번째로 큰 수 더하기

print(result)
