import sys
print(True if (a := int(sys.stdin.readline())) % 13 == 0 or a % 19 == 0 else False)