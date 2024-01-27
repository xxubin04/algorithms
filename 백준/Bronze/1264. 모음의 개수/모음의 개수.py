input = open(0).readline

while True:
    cnt = 0
    words = list(input().strip())
    if words == ['#']:
        break
    for i in words:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    print(cnt)