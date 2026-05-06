from collections import Counter

def solution(want, number, discount):
    ans = 0
    target = dict(zip(want, number))
    cnt = Counter(discount[:10])
    
    for i in range(len(discount) - 9):
        if all(cnt.get(w, 0) >= target[w] for w in want):
            ans += 1
        
        if i + 10 < len(discount):
            left = discount[i]
            right = discount[i+10]
            
            cnt[left] -= 1
            if cnt[left] == 0:
                del cnt[left]
            
            cnt[right] += 1
    
    return ans