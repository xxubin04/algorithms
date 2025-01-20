def solution(wordfind, N, ring):
    answer = 0
    for r in ring:
        double_ring = r + r
        if wordfind in double_ring:
            answer += 1
    return answer
