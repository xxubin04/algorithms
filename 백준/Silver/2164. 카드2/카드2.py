N = int(input())
i = 2

if N == 1 or N == 2:
    print(N)
    exit()

for _ in range(1000):
    i *= 2
    if i >= N:
        print((N - (i // 2)) * 2)
        break