def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    video_len_sec = int(video_len[:2]) * 60 + int(video_len[3:])
    op_start_sec = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end_sec = int(op_end[:2]) * 60 + int(op_end[3:])
    pos_sec = int(pos[:2]) * 60 + int(pos[3:])
    
    for cmd in commands:
        if op_start_sec <= pos_sec < op_end_sec:
            pos_sec = op_end_sec
        
        if cmd == "prev":
            pos_sec -= 10
            if pos_sec < 0: 
                pos_sec = 0
        elif cmd == "next":
            pos_sec += 10
            if pos_sec > video_len_sec:
                pos_sec = video_len_sec
                
    if op_start_sec <= pos_sec < op_end_sec:
            pos_sec = op_end_sec
        
    m = ('0' + str(pos_sec // 60))
    m = m[len(m)-2:len(m)]
    s = ('0' + str(pos_sec % 60))
    s = s[len(s)-2:len(s)]
    
    answer = m + ":" + s
    
    return answer