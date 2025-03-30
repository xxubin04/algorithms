croatia_alpabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

cnt = 0
i = 0
word = input().rstrip()

while i < len(word):
    if word[i:i+3] == "dz=":
        cnt += 1
        i += 3
    elif word[i:i+2] in croatia_alpabet:
        cnt += 1 
        i += 2
    else:
        cnt += 1 
        i += 1 

print(cnt)