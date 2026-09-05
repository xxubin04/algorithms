from collections import Counter

def solution(participant, completion):
    participant, completion = Counter(participant), Counter(completion)
    
    for name in participant:
        if participant[name] == completion[name]:
            continue
        
        return name