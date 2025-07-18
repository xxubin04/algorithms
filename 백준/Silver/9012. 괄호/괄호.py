import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    stk = []
    parenthesis = list(sys.stdin.readline().rstrip())

    for p in parenthesis:
        if stk and p != stk[-1] and stk[-1] == '(':  # 짝이라면
            stk.pop()
        else:  # stk에 아무것도 없거나 짝이 아니라면
            stk.append(p)

    if stk:
        print("NO")
    else:
        print("YES")