def solution(answers):
    ans = []
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if p1[i % 5] == answers[i]:
            score[0] += 1
        if p2[i % 8] == answers[i]:
            score[1] += 1
        if p3[i % 10] == answers[i]:
            score[2] += 1
            
    max_cnt = max(score)
    for j in range(3):
        if score[j] == max_cnt:
            ans.append(j+1)
    
    return ans