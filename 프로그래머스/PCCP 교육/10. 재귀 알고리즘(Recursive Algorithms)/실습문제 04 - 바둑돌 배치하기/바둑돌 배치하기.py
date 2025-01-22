import math as m
def f(low, col):
    if low % 2 == 1 and col % 2 == 1:
        return 1 + 4 * f(m.floor(low/2), m.floor(col/2))
    else:
        return 0

low, col = map(int, input().split())
print(f(low, col))
