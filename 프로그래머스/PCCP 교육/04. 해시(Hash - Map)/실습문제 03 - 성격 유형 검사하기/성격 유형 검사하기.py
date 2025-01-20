def solution(survey, choices):
    answer = ''
    scores = {"R": 0, "T": 0,
              "C": 0, "F": 0,
              "J": 0, "M": 0,
              "A": 0, "N": 0}
    
    for i in range(len(survey)):
        if choices[i] >= 5:
            scores[survey[i][1]] += (choices[i] - 4)
        elif choices[i] <= 3:
            scores[survey[i][0]] += (4 - choices[i])
            
    scores_list = [[], [], [], []]
    
    num = 0  # 지표 번호
    for k, v in scores.items(): 
        scores_list[num // 2].append((k, v))
        num += 1
        
    for j in range(4):
        if scores_list[j][0][1] > scores_list[j][1][1]:
            answer += scores_list[j][0][0]
        elif scores_list[j][0][1] < scores_list[j][1][1]:
            answer += scores_list[j][1][0]
        else:
            answer += scores_list[j][0][0]
        
    return answer
