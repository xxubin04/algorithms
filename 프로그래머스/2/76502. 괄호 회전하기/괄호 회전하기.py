def solution(s):
    ans = 0
    pair = {']': '[', ')': '(', '}': '{'}
    
    def check(s):
        for j in range(l):
            if (a := s[j]) in [']', ')', '}']:
                if not stk:  # 닫힌 괄호인데 스택이 비어있다면
                    return False 
                if pair[a] not in stk:  # 쌍인 열린 괄호가 스택에 없다면 
                    return False
                if stk[-1] == pair[a]:  # 스택의 마지막에 쌍이 있다면
                    stk.pop()
            else:
                stk.append(a)  # 열린 괄호는 스택에 추가 
        
        return False if stk else True
                    
        
    for i in range(l := len(s)):
        rotated = s[i:] + s[:i]
        stk = []
        ans += 1 if check(rotated) else 0
    
    return ans