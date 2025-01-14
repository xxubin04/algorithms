student = int(input())
state = list(map(int, input().split()))

n = int(input())
for _ in range(n):
    info = list(map(int, input().split()))
    mul = info[1] - 1
    if info[0] == 1:
        while mul <= student-1:
            state[mul] = 0 if state[mul] == 1 else 1
            # mul += (mul+1)
            mul += info[1]
    else:
        start, end = mul-1, mul+1
        state[mul] = 0 if state[mul] == 1 else 1
        while 0 <= start and end <= student-1:
            if state[start] == state[end]:
                if state[start] == 0:
                    state[start], state[end] = 1, 1
                else:
                    state[start], state[end] = 0, 0
                start -= 1; end += 1
            else:
                break

for i in range(0, student, 20):
    print(*state[i:i + 20])