import sys
if (n := int(sys.stdin.readline())) == 2:
    print(28)
elif n in [1,3,5,7,8,10,12]:
    print(31)
else:
    print(30)