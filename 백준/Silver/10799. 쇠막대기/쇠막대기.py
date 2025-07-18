import sys

stk = []
piece = 0
prior = ''

for p in (parenthesis := list(sys.stdin.readline().rstrip())):
    if stk and p == ')' and prior == '(' and stk[-1] == '(':  # 레이저라면
        stk.pop()
        piece += len(stk)
    elif stk and p == ')' and prior == ')' and stk[-1] == '(':  # 쌍은 맞지만 레이저는 아니라면
        stk.pop()
        piece += 1
    else:
        stk.append(p)

    prior = p

print(piece)