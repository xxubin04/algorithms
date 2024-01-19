input = open(0).readline

prime = [0, 0] + [1] * 999999
for j in range(2, 1001):
    if prime[j]:
        for k in range(j*2, 1000001, j):
            prime[k] = 0
prime[2] = 0

while True:
    flag = False
    num = int(input())
    if num == 0:
        break
    for i in range(3, num//2+1, 2):
        if prime[i] and prime[num-i]:
            print(f"{num} = {i} + {num-i}")
            flag = True
            break
    if flag == False:
        print("Goldbach's conjecture is wrong.")