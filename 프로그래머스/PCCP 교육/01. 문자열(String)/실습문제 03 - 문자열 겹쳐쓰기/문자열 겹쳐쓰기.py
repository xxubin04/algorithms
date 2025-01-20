def solution(my_string, overwrite_string, s):
    start = my_string[:s]
    end = my_string[s + len(overwrite_string) : ]
    
    answer = start + overwrite_string + end
    return answer
