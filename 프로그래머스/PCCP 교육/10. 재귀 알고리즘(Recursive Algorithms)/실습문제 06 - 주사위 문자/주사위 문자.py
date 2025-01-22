def f(i, n, case, st):
    if i == n:
        print(case)
        return 
    for j in range(len(st)):
        f(i+1, n, case+st[j], st)

n = int(input())
st = input()

f(0, n, "", st)
