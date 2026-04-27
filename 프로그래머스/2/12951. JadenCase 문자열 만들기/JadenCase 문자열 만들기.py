def solution(s):
    for idx, w in enumerate(words := list(s.split(" "))):
        if w == "":
            continue
        elif w[0].isalpha():  # 맨 앞 글자가 알파벳이라면
            words[idx] = w[0].upper() + w.lower()[1:]
        else:  # 맨 앞 글자가 알파벳이 아니라면
            words[idx] = w[0] + w.lower()[1:]
    return ' '.join(words)