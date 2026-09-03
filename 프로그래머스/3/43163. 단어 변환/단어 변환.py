from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0] * (lw := len(words))
    
    def can_change(a, b):
        diff = 0 
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
                
        if diff == 1:  # 다른 글자수가 1개라면 True 반환 
            return True
        else:
            return False
    
    def bfs():
        q = deque([(begin, 0)])  # (단어, 단계)
    
        while q:
            word, phase = q.popleft()
            
            if word == target:
                return phase
            
            for i in range(len(words)):
                # 아직 방문하지 않았고 1자리만 다르다면
                if not visited[i] and can_change(word, words[i]):
                    q.append((words[i], phase+1))
                    visited[i] = 1
            
        return 0
    
    return bfs()
   