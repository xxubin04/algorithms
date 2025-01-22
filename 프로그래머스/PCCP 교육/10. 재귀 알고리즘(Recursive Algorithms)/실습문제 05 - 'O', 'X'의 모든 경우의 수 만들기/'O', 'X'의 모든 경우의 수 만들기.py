def f(cnt, n, str):
    if cnt == n:
        print(str)
        return

    f(cnt+1, n, str+'O')
    f(cnt+1, n, str+'X')

n = int(input())

f(0, n, '')
