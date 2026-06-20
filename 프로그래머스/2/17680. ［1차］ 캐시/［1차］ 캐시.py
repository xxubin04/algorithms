from collections import deque

def solution(cacheSize, cities):
    time = 0
    stk = deque([])
    # 캐시 크기가 0인 경우 
    if cacheSize == 0:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        if len(stk) < cacheSize:
            time += (1 if city in stk else 5)
            stk.append(city)
        elif len(stk) == cacheSize:
            if city in stk:
                stk.remove(city)
                stk.append(city)
                time += 1
            else:
                stk.popleft()
                stk.append(city)
                time += 5
    
    return time
            