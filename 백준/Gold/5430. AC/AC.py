import sys
from collections import deque

for _ in range(int(sys.stdin.readline().rstrip())):
    cmd = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())

    input_nums = sys.stdin.readline().rstrip()[1:-1]

    if len(input_nums) != 0:
        nums = deque(map(int, input_nums.split(',')))
    else:
        nums = deque()

    is_reversed = False
    error = False

    for c in cmd:
        if c == 'R':
            is_reversed = not is_reversed
        elif c == 'D' and not nums:
            error = True
            break
        elif c == 'D' and nums and is_reversed:
            nums.pop()
        else:
            nums.popleft()

    if error:
        print("error")
    else:
        if is_reversed:
            print('[' + ','.join(map(str, reversed(nums))) + ']')
        else:
            print('[' + ','.join(map(str, nums)) + ']')