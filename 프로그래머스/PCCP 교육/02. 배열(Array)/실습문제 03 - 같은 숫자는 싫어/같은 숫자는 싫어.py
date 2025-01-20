def solution(arr):
    answer = []
    for a in range(len(arr)):
        if a == 0:
            prior = arr[a]
            answer.append(arr[a])
        elif arr[a] != prior:
            answer.append(arr[a])
            prior = arr[a]
    return answer
