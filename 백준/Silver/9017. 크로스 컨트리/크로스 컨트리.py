input = open(0).readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    valid_nums = {}
    dict = {}
    min_score = 1e9

    # (선수의 수, 점수 총합, 5번째 선수의 점수)
    for i in range(n):
        if nums[i] not in dict:
            dict[nums[i]] = [1, 0, 0]
        else:
            dict[nums[i]][0] += 1

    for j in range(len(dict)):
        if dict[j+1][0] == 6:
            valid_nums[j+1] = 0

    score = 1
    for k in range(n):
        if nums[k] in valid_nums:
            valid_nums[nums[k]] += 1
            if valid_nums[nums[k]] == 5:
                dict[nums[k]][2] = score
            elif valid_nums[nums[k]] <= 4:
                dict[nums[k]][1] += score
            score += 1

    min_score_list = []
    sorted_dict = sorted(dict.items(), key=lambda x: (x[1][1], x[1][2]))

    for i in range(len(sorted_dict)):
        if sorted_dict[i][1][0] == 6:
            print(sorted_dict[i][0])
            break