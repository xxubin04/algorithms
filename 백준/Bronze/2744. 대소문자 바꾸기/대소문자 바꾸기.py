from sys import stdin as std

word = list(std.readline())
for i in range(len(word)):
    if word[i].isupper() == True:
        word[i] = word[i].lower()
    else:
        word[i] = word[i].upper()
for j in word:
    print(j, end='')