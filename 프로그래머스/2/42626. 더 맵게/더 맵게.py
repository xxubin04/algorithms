# from heapq import heappush, heappop, heapify
# def solution(scoville, K):
#     answer = 0
#     heapify(scoville)
#     while (spicy := heappop(scoville) < K and len(scoville) >= 2):
#         spicy += heappop(scoville) * 2
#         heappush(scoville, spicy)
#         answer += 1
#         if (a := heappop(scoville)) >= K:
#             return answer
#             break
#         else:
#             heappush(scoville, a)
#     if heappop(scoville) < K: return -1
#     return answer

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_scoville = first + second * 2
        heapq.heappush(scoville, new_scoville)

        answer += 1

    return answer
