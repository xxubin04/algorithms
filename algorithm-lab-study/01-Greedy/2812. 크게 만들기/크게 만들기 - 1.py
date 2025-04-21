N, K = map(int, input().split())
num = input().rstrip()

stack = []

for i in list(num):
    while K > 0 and stack:
        if i > stack[-1]:
            stack.pop()
            K -= 1
        else:
            break
    stack.append(i)

if K != 0:
    stack = stack[:len(stack)-K]

print(''.join(stack))
