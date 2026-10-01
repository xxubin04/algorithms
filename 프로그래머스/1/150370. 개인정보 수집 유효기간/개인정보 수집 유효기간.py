def solution(today, terms, privacies):
    term_dict = {}
    deadlines = []  # 개인정보들이 유효기간
    remove_list = []  # 파기해야 할 개인정보들
    
    # 약관과 유효기간 딕셔너리에 저장 
    for t in terms:
        term, month = t.split()
        term_dict[term] = int(month)
    
    for p in privacies:
        calendar, term = p.split()
        
        year = int(calendar[:4])
        month = int(calendar[5:7])
        day = int(calendar[8:])
        
        month += term_dict[term]  # 유효기간
        
        # 만약 OO월 01일이라면 유효기간이 28일이 됨
        day -= 1
        
        if day == 0:
            day = 28
            month -= 1
            
            if month == 0:  # 달이 0월이 된다면
                month = 12
                year -= 1
            
        year += (month - 1) // 12
        month = (month - 1) % 12 + 1
    
        deadlines.append((str(year).zfill(4))+'.'+(str(month).zfill(2))+'.'+(str(day).zfill(2)))
    
    for idx in range(len(deadlines)):
        if deadlines[idx] < today:  # 유효기간이 오늘보다 이전이라면
            remove_list.append(idx+1)
    
    return remove_list