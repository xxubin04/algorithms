a, b, c = int(input()), int(input()), int(input())
nums = list(str(a*b*c))

for i in range(10):
    print(nums.count(str(i)))