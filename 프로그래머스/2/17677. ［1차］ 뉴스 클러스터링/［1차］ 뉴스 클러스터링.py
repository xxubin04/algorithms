# from math import floor

# def solution(str1, str2):
#     answer = 0
#     list1, list2 = [], []
#     for a in range(len(str1)-1):
#         if (slice_a := str1[a:a+2]).isalpha():
#             list1.append(str1[a:a+2].upper())
#     for b in range(len(str2)-1):
#         if (slice_b := str2[b:b+2]).isalpha():
#             list2.append(str2[b:b+2].upper())
    
#     total = len(list1) + len(list2)
#     duplication = 0

#     for i in list1:
#         if i in list2:
#             list2.remove(i)
#             duplication += 1
            
#     if (len(list1) == 0 and len(list2) == 0) or total == duplication:
#         return 65536
    
#     answer = floor(duplication / (total - duplication) * 65536) 
        
#     return answer

from collections import Counter

def solution(str1, str2):
    str1_list = []
    str2_list = []
    
    for i in range(len(str1)-1):
        if (s := str1[i:i+2].upper()).isalpha():
            str1_list.append(s)
    
    for i in range(len(str2)-1):
        if (s := str2[i:i+2].upper()).isalpha():
            str2_list.append(s)
    
    # 둘 다 공집합이라면
    if len(str1_list) == len(str2_list) == 0:
        return 65536

    str1_Counter = Counter(str1_list)
    str2_Counter = Counter(str2_list)
    
    inter, union = 0, 0  # 교집합, 합집합의 원소 개수 
    
    for s1 in str1_Counter:
        # str1의 원소가 str2에도 있다면
        if s1 in str2_Counter:
            inter += min(str1_Counter[s1], str2_Counter[s1])  # 둘 중 최소 개수 증가         
            union += max(str1_Counter[s1], str2_Counter[s1])  # 둘 중 최대 개수 증가
        else:
            union += str1_Counter[s1]  # str2에 없으면 str1의 개수만큼 추가
    
    for s2 in str2_Counter:
        # str2에 있지만 str1에는 없는 원소의 개수만큼 추가
        if s2 not in str1_Counter:
            union += str2_Counter[s2]  # str1에 없으면 str2의 개수만큼 추가
    
    answer = int(inter / union * 65536)

    return answer
    
    