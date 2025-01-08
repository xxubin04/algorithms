input = open(0).readline

while True:
    lengths = sorted(list(map(int, input().split())))

    if lengths[2] == 0:
        break

    if lengths[2] >= lengths[0] + lengths[1]:
        print("Invalid")
    elif lengths[0] == lengths[1] == lengths[2]:
        print("Equilateral")
    elif lengths[1] == lengths[2] or lengths[0] == lengths[1]:
        print("Isosceles")
    else:
        print("Scalene")