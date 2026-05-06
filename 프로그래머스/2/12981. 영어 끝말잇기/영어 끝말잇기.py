def solution(n, words):
    prior = words[0][-1]  # 앞사람 단어의 마지막 문자
    used = [words[0]]  # 사용한 단어
    
    for i in range(1, len(words)):
        # 조건 3가지 전부 만족
        if ((w := words[i])[0] == prior) and (w not in used) and (len(w) != 1):
            used.append(w)
            print(prior, w)
            prior = w[-1]
            continue
        else:
            print(prior, w)
            return [n if (t := (i+1)%n) == 0 else t, (i+n)//n]
    
    return [0, 0]