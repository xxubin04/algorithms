from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length)  # 대기줄
    total = 0  # 현재의 무게합
    
    while trucks:
        answer += 1
        
        # 다리 맨 앞 차량 빠져나감
        out = bridge.popleft()
        total -= out
        
        # 다음 트럭을 올릴 수 있다면
        if total + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            total += truck
        else:
            bridge.append((0))  # 못 올리면 빈 공간
    
    answer += bridge_length
    
    return answer