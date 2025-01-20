def solution(s):
    answer = ""
    num_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in range(len(s)):
        if s[i] in num_dict.values():
            answer += s[i]
        else:
            for n in range(i, len(s)+1):
                if s[i:n] in num_dict.keys():
                    answer += num_dict[s[i:n]]
                    
    return int(answer)
