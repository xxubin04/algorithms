def solution(n, arr1, arr2):
    answer = [bin(a|b) for a, b in zip(arr1, arr2)]
    
    for i in range(n):
        answer[i] = answer[i][2:]
        answer[i] = answer[i].replace("1", "#")
        answer[i] = answer[i].replace("0", " ")
        
        answer[i] = answer[i].rjust(n, " ")
    return answer