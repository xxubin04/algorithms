input = open(0).readline

area = 0
dots = []
for i in range(N := int(input())):
    dots.append(tuple(map(int, input().split())))
    area += (dots[i-1][0] * dots[i][1] - dots[i][0] * dots[i-1][1]) if i >= 1 else 0
dots.append(dots[0])
area += (dots[N-1][0] * dots[N][1] - dots[N][0] * dots[N-1][1])
print(abs(round(area * 0.5, 2)))