N = int(input())
while N != 1:
    i = 2
    while N % i != 0:
        i += 1 
    print(i)
    N /= i