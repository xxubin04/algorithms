input = open(0).readline

num = 1
for _ in range(3):
    num *= int(input())
for a in range(10):
    print(list(str(num)).count(str(a)))