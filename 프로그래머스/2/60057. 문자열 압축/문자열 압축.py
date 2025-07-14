def solution(s):
    answer = len(s)

    for i in range(1, len(s)+1):
        prior = ''
        cnt_list = []
        seq_cnt = 1
        word_list = []
        
        for j in range(0, len(s), i):
            split_s = s[j:j+i]
            if prior == split_s:
                seq_cnt += 1
            else:
                prior = split_s
                cnt_list.append(seq_cnt)
                seq_cnt = 1
            word_list.append(split_s)
        cnt_list.append(seq_cnt)
        cnt_list.pop(0)
        cnt = 0

        while cnt_list:
            if len(cnt_list) == 1 and cnt_list[0] == 1:
                cnt += len(str(word_list[0]))
                cnt_list.pop()
            elif (c := cnt_list.pop(0)) == 1:
                cnt += i
                word_list.pop(0)
            else:
                cnt += (i + len(str(c)))
                word_list = word_list[c:]

        if cnt < answer:
            answer = cnt 
        
    return answer