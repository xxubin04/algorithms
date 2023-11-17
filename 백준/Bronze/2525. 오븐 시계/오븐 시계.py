H, M = map(int, input().split())
T = int(input())

sum = M + T
plus_H = sum//60
change_M = sum%60


if sum >= 60:
    Hour = H+plus_H
    if Hour // 24 >= 1:
        print(Hour%24, change_M)
    else:
        print(Hour, change_M)
else:
    print(H, M+T)