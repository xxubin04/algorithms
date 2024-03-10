input = open(0).readline

injured_finger = int(input())
enable_num = int(input())
ans =  0

if (enable_num == 0):
    print(injured_finger - 1)
else:
    if injured_finger == 1:
        ans += (8 * enable_num)
    elif injured_finger == 5:
        ans += (8 * enable_num) + 4
    elif enable_num % 2 == 0:   
        ans += 4 * (enable_num - 1) + 5 + (injured_finger - 2)
    else:                
        ans += 4 * (enable_num - 1) + 5 + (4 - injured_finger)
    print(ans)