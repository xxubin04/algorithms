input = open(0).readline

i = 1

while sum(nums := list(map(int, input().split()))):
    L, P, V = nums[0], nums[1], nums[2]
    if (V % P) >= L:
        print(f"Case {i}: {L * (V // P) + L}")
    else:
        print(f"Case {i}: {L * (V // P) + (V % P)}")
    i += 1