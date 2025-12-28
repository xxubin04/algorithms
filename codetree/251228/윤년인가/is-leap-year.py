import sys

if (year := int(sys.stdin.readline())) % 4 == 0 and not(year % 100 == 0 and year % 400 != 0):
    print("true")
else:
    print("false")