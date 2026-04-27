def solution(s):
    stk = []
    
    for p in s:
        if not stk:  # 스택이 비어있다면
            if p == ')':  # 추가하려는 괄호가 )이라면
                return False
            else:
                stk.append('(')
        elif stk[-1] == '(':  # 스택의 가장 최근 괄호가 (이라면
            if p == ')':
                stk.pop()
            else:
                stk.append('(')
    
    if stk:
        return False 
        
    return True