import sys

print("yes" if (a := int(sys.stdin.readline())) < 10 or a > 20 else "no")