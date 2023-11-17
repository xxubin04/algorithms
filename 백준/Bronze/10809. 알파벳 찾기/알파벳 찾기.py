aList=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
bList=[-1 for _ in range(26)]

S = list(input())

for i in range(len(S)):
    # if S[i] in aList:
    if bList[aList.index(S[i])] == -1:
        bList[aList.index(S[i])] = i
    else:
        continue

for j in bList:
    print(j, end=" ")