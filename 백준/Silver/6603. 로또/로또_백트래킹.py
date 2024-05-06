input = open(0).readline 

def backTracing(numComb, comb):
    if len(comb) == 6:
        print(" ".join(map(str, comb)))
        return
    for i in numComb[1:]:
        if i not in comb and i > comb[-1]:
            comb.append(i)
            backTracing(numComb, comb)
            comb.pop()
            
while (numComb := list(map(int, input().split()))) != [0]:
    comb = []
    for start in range(1, numComb[0]-4):
        backTracing(numComb, [numComb[start]])
    print()
