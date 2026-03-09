n = int(input())

i = 0
for _ in range(n):
    for _ in range(n):
        print((i % 9 + 1), end=' ')
        i += 1
    print()