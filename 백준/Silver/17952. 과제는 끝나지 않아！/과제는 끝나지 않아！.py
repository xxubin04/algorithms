from sys import stdin

score = 0; stack = []
N = int(stdin.readline())

for n in range(1, N+1):
    aList = list(map(int, stdin.readline().split()))
    if aList[0] == 1:
        A = aList[1]; T = aList[2]
        stack.append([n, A, T])
        if stack[-1][-1] == 1:
            score += stack[-1][1]
            stack.pop(-1)
        else:
            stack[-1][-1] -= 1
    else:
        if not stack:
            pass
        else:
            if stack[-1][-1] == 1:
                score += stack[-1][1]
                stack.pop(-1)
            else:
                stack[-1][-1] -= 1
print(score)