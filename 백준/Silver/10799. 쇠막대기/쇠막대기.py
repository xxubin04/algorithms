import sys

stk = []
piece = 0
prior = ''

for p in list(sys.stdin.readline().rstrip()):
    if stk and p == ')' and stk[-1] == '(':
        if prior == '(':
            stk.pop()
            piece += len(stk)
        else:      
            stk.pop()
            piece += 1
    else:
        stk.append(p)

    prior = p

print(piece)
