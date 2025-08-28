def solution(diffs, times, limit):
    def is_possible(level):
        taken_time = 0
        time_prev = 0
        
        for i in range(len(diffs)):
            time_cur = times[i]
            diff = diffs[i]
            
            if level >= diff:
                taken_time += time_cur
            else:
                taken_time += (time_cur + time_prev) * (diff - level) + time_cur
            
            if taken_time > limit:
                return False
            
            time_prev = time_cur
        
        return True

    ans = -1
    start, end = min(diffs), max(diffs)

    while start <= end:
        mid = (start + end) // 2
        
        if is_possible(mid):
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans

#     ans = -1
#     start, end = min(diffs), max(diffs)
    
#     while start <= end:
#         level = (start + end) // 2
#         taken_time = 0
#         time_prev = 0
#         flag = True  # 모든 퍼즐 게임을 다 순회했는지 여부 
        
#         # print("start: ", start, " level: ", level, " end: ", end)
    
#         for idx in range(len(diffs)):
#             if taken_time > limit:  # 걸리는 시간이 제한 시간을 넘었다면
#                 start = level + 1  # level 키워야 함 
#                 print("too low level")
#                 flag = False  
#                 # print(start, end, level)
#                 break

#             time_cur = times[idx]  # 현재 퍼즐의 시간 
#             diff = diffs[idx]  # 현재 퍼즐의 난이도 

#             if (level >= diff):
#                 taken_time += time_cur
#             else:
#                 taken_time += ((time_cur + time_prev) * (diff - level) + time_cur)
            
#             time_prev = time_cur
#             # print("taken_time: ", taken_time, " limit: ", limit)
        
#         if flag and taken_time <= limit:
#             ans = level
#             end = level - 1
        
#     return ans