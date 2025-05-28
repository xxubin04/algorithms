input = open(0).readline

dots = []

for i in range(n := int(input())):
    x, y = map(int, input().split())
    dots.append((x, 1))
    dots.append((y, -1))

dots.sort()

cnt = 0
total = 0

for n, d in dots:
    cnt += d
    if cnt == 1 and d == 1:  # start면서 겹치는 것 X
        start = n
    elif cnt == 0 and d == -1:  # end면서 겹치는 것 X
        end =  n
        total += (end - start)

print(total)