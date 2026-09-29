def solution(word):
    num = 0  # 몇 번째 단어인지
    
    def dfs(current):
        nonlocal num
        
        # 길이가 이미 5라면 더 이상 문자를 붙일 수 없음
        if len(current) == 5:
            return False 
        
        for v in ['A', 'E', 'I', 'O', 'U']:
            next_word = current + v
            num += 1
            
            if next_word == word:
                return True 
            
            if dfs(next_word):
                return True
    
        return False

    dfs('')
    return num
            