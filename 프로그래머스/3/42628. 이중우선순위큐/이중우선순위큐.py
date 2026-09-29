import heapq

def solution(operations):
    heap = []
    
    for o in operations:
        op, num = o.split()
        num = int(num)
        
        if op == 'I':  # 삽입하는 명령어라면
            heapq.heappush(heap, num)
        else:  # 삭제하는 명령어라면
            if len(heap) == 0:  # 힙이 비어있다면 
                continue
            
            if num == 1:  # 최댓값을 삭제한다면
                heap.remove(max(heap))
            else:  # 최솟값을 삭제한다면
                heapq.heappop(heap)
    
    if not heap:  # 큐가 비어있다면
        return([0, 0])
    else:  # 큐가 안 비어있다면
        return([int(max(heap)), int(heapq.heappop(heap))])
                
    