N = int(input())
arr = [5*i for i in range(N // 5, -1, -1)]

for j in range(len(arr)):
    if (div := N - arr[j]) == 0:
        print(len(arr) - j - 1)
        quit()
    elif div % 3 == 0:
        print((len(arr) - j - 1) + (div // 3))
        quit()

print(-1)