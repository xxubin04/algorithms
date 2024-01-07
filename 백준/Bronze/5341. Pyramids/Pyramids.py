while 1:
    total = 0
    num = int(input())
    if num != 0:
        for i in range(1, num+1):
            total += i
        print(total)
    else:
        break