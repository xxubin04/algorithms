def solution(participant, completion):
    success = {}
    for p in participant:
        if p in success:
            success[p] += 1
        else:
            success[p] = 1
    
    for c in completion:
        success[c] -= 1
        
    for name, num in success.items():
        if num != 0:
            return name
