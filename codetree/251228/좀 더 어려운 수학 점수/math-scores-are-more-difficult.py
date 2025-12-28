import sys
a_math, a_eng = map(int, sys.stdin.readline().split())
b_math, b_eng = map(int, sys.stdin.readline().split())

if a_math == b_math:
    if a_eng > b_eng:
        print("A")
    else:
        print("B")
elif a_math > b_math:
    print("A")
else:
    print("B")