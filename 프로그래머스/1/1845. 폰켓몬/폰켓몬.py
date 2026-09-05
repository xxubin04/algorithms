# (N_C_N//2) -> 조합 
# 최대한 다양한 포켓몬을 가질 때의 포켓몬 종류 반환
from collections import Counter

def solution(nums):
    sort_num = len(Counter(nums))  # 폰켓몬 종류의 수
    N = len(nums)  # 폰켓몬 수
    
    # 골라야 하는 폰켓몬 수 (N//2)보다 종류의 수가 작거나 같다면, 종류의 수 반환
    return sort_num if sort_num <= N // 2 else N // 2