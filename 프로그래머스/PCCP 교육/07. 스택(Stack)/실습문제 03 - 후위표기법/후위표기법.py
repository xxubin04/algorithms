stk = []
n = int(input())
cal = list(input().split())

for i in cal:
    if i.isdigit():
        stk.append(int(i))
    elif i == '+':
        stk.append(stk.pop() + stk.pop())
    elif i == '-':
        n1 = stk.pop()
        n2 = stk.pop()
        stk.append(n2 - n1)
    elif i == '*':
        stk.append(stk.pop() * stk.pop())
    elif i == '/':
        n1 = stk.pop()
        n2 = stk.pop()
        stk.append(n2 // n1)

print(stk.pop())
