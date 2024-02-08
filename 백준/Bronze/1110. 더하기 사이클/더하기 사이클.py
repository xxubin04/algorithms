n = int(input())
cnt = 0
a = n

while True:
    new = int(str(a)[-1] + str(sum(map(int, list(str(a)))))[-1])
    a = new
    if n != new:
        cnt += 1
    else:
        print(cnt+1)
        break