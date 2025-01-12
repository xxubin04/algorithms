input = open(0).readline

part = 0
waist = 0
left_arm, right_arm = 0, 0
left_leg, right_leg = 0, 0
for n in range(N := int(input())):
    row = list(input().rstrip())
    if "*" in row:
        if part == 0:  # 머리
            part += 1
            head_idx = row.index('*')  # 머리의 열 위치 저장
            print(n+2, head_idx+1)
        elif part == 1:  # 팔, 심장
            part += 1
            left_arm = head_idx - row.index('*')
            right_arm = row.index('*') + row.count('*') - head_idx - 1
        elif part == 2 and row.count('*') == 1:  # 허리
            waist += 1
        elif part == 2 and row.count('*') != 1:
            part += 1

        if part == 3 and row.count('*') == 2:
            left_leg += 1
            right_leg += 1
        elif part == 3 and row.count('*') == 1:
            if row.index('*') == head_idx - 1:
                left_leg += 1
            else:
                right_leg += 1

print(left_arm, right_arm, waist, left_leg, right_leg)