import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    valid = [False] * len(operations)

    for i, operation in enumerate(operations):
        op, num = operation.split()
        num = int(num)

        # 삽입
        if op == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            valid[i] = True

        # 삭제
        else:
            if num == 1:
                # 이미 삭제된 값 제거
                while max_heap and not valid[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    _, idx = heapq.heappop(max_heap)
                    valid[idx] = False

            else:
                # 이미 삭제된 값 제거
                while min_heap and not valid[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    _, idx = heapq.heappop(min_heap)
                    valid[idx] = False

    # 마지막으로 삭제된 값 정리
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]