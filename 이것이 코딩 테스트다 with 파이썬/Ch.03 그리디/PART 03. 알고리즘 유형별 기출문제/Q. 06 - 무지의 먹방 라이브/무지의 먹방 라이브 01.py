# 이것이 코테다 p.316
# Ch.11 그리디
# 기출 문제 - 06. 무지의 먹방 라이브
# 걸린 시간: 15분 + a
# 일시: 2025.02.02
### 정확성 테스트 100% 통과, 효율성 테스트 0% 통과

def solution(food_times, k):
    if sum(food_times) <= k:  # 남은 전체 음식 양이 k보다 작으면 중단
        return -1

    idx = 0
    while k > 0:
        if sum(food_times) == 0:  # 모든 음식이 0이면 종료
            return -1
        
        if food_times[idx % len(food_times)] > 0:  # 음식이 남아있다면 감소
            food_times[idx % len(food_times)] -= 1
            k -= 1
        idx += 1
    
    while food_times[idx % len(food_times)] == 0:   # 다음 먹어야 할 음식 찾기
        idx += 1
    
    return (idx % len(food_times)) + 1
