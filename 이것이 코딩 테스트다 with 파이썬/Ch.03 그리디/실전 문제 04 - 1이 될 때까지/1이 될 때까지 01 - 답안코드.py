N, K = map(int, input().split())
cnt = 0  # 과정 수행 횟수 

while True:
  target = (N // K) * K  # K로 나누어 떨어지는 최대한의 수
  cnt += (N - target)  # 1을 빼는 횟수만큼 더하기
  N = target  # N을 target으로 갱신 (나누어 떨어질때까지 1을 뺐으므로)
  if N < K:  # N이 K보다 작아지면
    break  # 반복문 탈출 
  cnt += 1  # N이 target(K의 배수)이라면 횟수 +1
  N //= K  # N을 K로 나눈 몫으로 N 갱신 

cnt += (N - 1)  # 반복문 탈출 후, 나머지만큼 -1 반복
print(cnt)
