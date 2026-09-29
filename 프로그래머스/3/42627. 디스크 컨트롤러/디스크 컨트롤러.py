import heapq

def solution(jobs):
    jobs.sort()
    
    heap = []
    current = 0  # 현재 시간
    total = 0
    idx = 0
    n = len(jobs)
    
    while idx < n or heap:
        
        # 현재 시간까지 요청된 작업을 힙에 추가
        while idx < n and jobs[idx][0] <= current:
            request_time, duration = jobs[idx]
            
            heapq.heappush(
                heap,
                (duration, request_time, idx)
            )
            idx += 1
            
        # 처리 가능한 작업이 있다면
        if heap:
            duration, request_time, job_num = heapq.heappop(heap)
        
            current += duration
            total += current - request_time
        else:  # 처리할 작업이 없다면 다음 요청 시간으로 이동
            current = jobs[idx][0]
        
    return total // n