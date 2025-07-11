import sys

first = int(sys.stdin.readline().rstrip())
max_nums = []

for second in range(first+1):
    prior = first
    next = second
    nums = [prior, next]
    while (following := prior - next) >= 0:
        nums.append(following)
        prior = next
        next = following
    if len(nums) > len(max_nums):
        max_nums = nums

print(len(max_nums))
print(*max_nums)