# 답안코드 참고해서 풂
n = int(input())
coins = sorted(list(map(int, input().split())))

target = 1  #  만들 수 있는 최대 금액 + 1)
for coin in coins:
  if target < coin:
    break
  target += coin

print(target)
