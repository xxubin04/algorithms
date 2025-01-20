def solution(s):
    answer = ''
    words = list(s.split(" "))
    for word in words:
        for j in range(len(word)):
            if j % 2 == 0:
                answer += word[j].upper()
            elif j % 2 != 0:
                answer += word[j].lower()
            else:
                answer += word[j]
        answer += " "
    return answer[:-1]
