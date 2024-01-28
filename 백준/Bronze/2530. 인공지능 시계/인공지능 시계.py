input = open(0).readline

h, m, s = map(int, input().split())
time = int(input())

h += time//3600
time = time%3600
m += time//60
time = time%60
s += time
if s >= 60:
    s -= 60
    m += 1
if m >= 60:
    m -= 60
    h += 1
if h//24 >= 1:
    h %= 24
print(h, m, s)