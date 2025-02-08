nums = []
for i in range(n := int(input())):
    if (num := int(input())) == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))