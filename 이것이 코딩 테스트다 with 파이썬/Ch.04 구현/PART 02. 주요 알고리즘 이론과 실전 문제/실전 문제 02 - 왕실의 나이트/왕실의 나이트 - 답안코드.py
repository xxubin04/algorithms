location = list(input().rstrip())
x, y = int(location[1]), ord(location[0]) - ord('a') + 1
answer = 0

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

for step in steps:
  nx = x + step[0]
  ny = y + step[1]

  if 1 <= nx <= 8 and 1 <= ny <= 8:
    answer += 1

print(answer)
