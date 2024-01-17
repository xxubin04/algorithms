n = int(input())
for i in range(n):
    pw = input()
    if len(pw) >= 6 and len(pw) <= 9:
        print('yes')
    else:
        print('no')