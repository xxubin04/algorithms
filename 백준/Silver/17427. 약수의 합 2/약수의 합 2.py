import sys

answer = 0

for i in range(1, (n := int(sys.stdin.readline())) + 1):
    answer += i * (n // i)

print(answer)