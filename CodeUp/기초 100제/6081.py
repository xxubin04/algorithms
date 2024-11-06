input = open(0).readline

a = int(input(), 16)

for i in range(1, 16):
    print("%X*%X=%X" %(a, i, a*i))
