from sys import stdin

test = int(stdin.readline())
for _ in range(test):
    A_num, B_num = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))
    A.sort(reverse=True); B.sort(reverse=True)
    start = 0; pair = 0
    A_index = 0; B_index = 0

    while A_index < A_num and B_index < B_num:
        if A[A_index] > B[B_index]:
            pair += B_num - B_index
            A_index += 1
        else:
            B_index += 1
    print(pair)