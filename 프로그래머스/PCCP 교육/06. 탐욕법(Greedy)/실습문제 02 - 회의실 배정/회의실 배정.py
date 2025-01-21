def solution(arr):
    arr.sort(key=lambda x: (x[1], x[0]))

    time, cnt = 0, 0

    for start, end in arr:
        if start >= time:
            time = end
            cnt += 1

    return cnt
