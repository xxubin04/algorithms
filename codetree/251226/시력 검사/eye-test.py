import sys

r = float(sys.stdin.readline())
if ((l := float(sys.stdin.readline())) >= 1 and r >= 1):
    print("High")
elif (l >= 0.5 and r >= 0.5):
    print("Middle")
else:
    print("Low")