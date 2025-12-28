import sys
if ((n := int(sys.stdin.readline())) % 3 == 0 and n % 2 == 1) or (n % 5 == 0 and n % 2 == 0):
    print("true")
else:
    print("false")