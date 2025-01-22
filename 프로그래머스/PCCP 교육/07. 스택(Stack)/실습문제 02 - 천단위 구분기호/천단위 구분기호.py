stk = []
n, num = int(input()), input().strip()

for i in range(1, n+1):
    stk.append(num[i * (-1)])
    if i % 3 == 0 and i != n:
        stk.append(',')

for j in stk[::-1]:
    print(j, end='')
