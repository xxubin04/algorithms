from itertools import permutations
input = open(0).readline

A, B = input().split()
num_A = list(A)
perm_A = list(permutations(num_A, len(A)))

ans = -1
for i in perm_A:
    if i[0] == '0':
        continue

    if int(''.join(i)) < int(B):
        ans = max(ans, int(''.join(i)))

print(ans)