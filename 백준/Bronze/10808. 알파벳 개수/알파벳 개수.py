alpha = [0] * 26

for i in list(input()):
    alpha[ord(i) - 97] += 1

for j in range(26):
    print(alpha[j], end=' ')