a = list(input())
mid = len(a)//2

if len(a)%2 == 0:  # 짝수
    mid -= 1
    if a[:mid+1] == a[-1:mid:-1]:
        print(1)
    else:
        print(0)
else:
    if a[:mid] == a[-1:mid:-1]:  # 홀수
        print(1)
    else:
        print(0)