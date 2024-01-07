def cal(n):
    global total
    while n != 0:
        total += n
        n -= 1
    return total

while True:
    total = 0
    num = int(input())
    if num != 0:
        print(cal(num))
    else:
        break