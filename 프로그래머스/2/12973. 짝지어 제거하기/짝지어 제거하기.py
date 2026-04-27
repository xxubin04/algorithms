def solution(s):
    stk = []
    
    for w in s:
        # 스택이 비었거나
        # 스택의 가장 최근 문자와 동일하지 않다면 추가
        if not stk or w != stk[-1]:
            stk.append(w)
        elif w == stk[-1]:  # 스택의 가장 최근 문자와 동일하다면 제거
            stk.pop()
    
    return 1 if not stk else 0
                
        