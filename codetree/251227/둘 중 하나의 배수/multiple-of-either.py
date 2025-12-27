import sys
print(1 if (a := int(sys.stdin.readline())) % 3 == 0 or a % 5 == 0 else 0)