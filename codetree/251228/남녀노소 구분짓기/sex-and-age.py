import sys
gender, age = int(sys.stdin.readline()), int(sys.stdin.readline())
if gender == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")
elif age >= 19:
    print("WOMAN")
else:
    print("GIRL")