import sys

stk = [1]
not_yet_push = 2  # 아직 스택에 넣지 않은 수 중에서 최솟값
op = ['+']
flag = True

for i in range((n := int(sys.stdin.readline()))):
    num = int(sys.stdin.readline())

    if len(stk) == 0 and not_yet_push <= num:
        stk.append(not_yet_push)
        op.append('+')
        not_yet_push += 1
    elif len(stk) == 0 and not_yet_push > num:
        print("NO")
        exit()

    while stk:
        if stk[-1] == num:
            stk.pop()
            op.append('-')
            break
        elif stk[-1] > num:
            stk.pop()
            op.append('-')
        elif stk[-1] < num:  # 스택의 top이 pop하고자 하는 수보다 작은 경우
            if not_yet_push > num :  # 아직 넣지 않은 수들 중 최솟값이 pop하고자 하는 수보다 큰 경우
                print("NO")
                exit()
            else:  # 아직 넣지 않은 수들 중 회솟값이 pop하고자 하는 수보다 작은 경우
                stk.append(not_yet_push)
                op.append('+')
                not_yet_push += 1

for p in op: print(p)
