import sys
if 3 <= (m := int(sys.stdin.readline())) <= 5:
    print("Spring")
elif 6 <= m <= 8:
    print("Summer")
elif 9 <= m <= 11:
    print("Fall")
else:
    print("Winter")