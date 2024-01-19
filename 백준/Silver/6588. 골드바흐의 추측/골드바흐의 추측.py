input = open(0).readline

prime = [0, 0] + [1] * 999999
for j in range(2, 1001):
    if prime[j] == 1:
        for k in range(j*2, 1000001, j):
            prime[k] = 0
prime[2] = 0

num = int(input())
while num != 0:
    for i in range(len(prime)):
        if prime[i] == 1 and prime[num - i] == 1:
            print(f"{num} = {i} + {num-i}")
            break
    num = int(input())