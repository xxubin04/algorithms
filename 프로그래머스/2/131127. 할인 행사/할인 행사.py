# from collections import Counter

# def solution(want, number, discount):
#     want_counter = Counter(dict(zip(want, number)))
#     window_size = sum(number)

#     discount_counter = Counter(discount[:window_size])

#     answer = 0

#     if want_counter == discount_counter:
#         answer += 1

#     for i in range(window_size, len(discount)):
#         # 윈도우에서 빠지는 상품
#         discount_counter[discount[i - window_size]] -= 1

#         # 개수가 0이 되면 삭제
#         if discount_counter[discount[i - window_size]] == 0:
#             del discount_counter[discount[i - window_size]]

#         # 새로 들어오는 상품
#         discount_counter[discount[i]] += 1

#         if want_counter == discount_counter:
#             answer += 1

#     return answer



from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    food_dict = defaultdict(int)
    want_dict = defaultdict(int)
    
    for w, n in zip(want, number):
        want_dict[w] = n
    
    # 처음 9개
    for f in discount[:10]:
        food_dict[f] += 1
    
    if want_dict == food_dict:
        answer += 1

    s, e = 0, 10
    
    while e < len(discount):
        food_dict[discount[s]] -= 1
        food_dict[discount[e]] += 1
        
        if food_dict[discount[s]] == 0:
            del food_dict[discount[s]]
        
        s += 1
        e += 1
        
        if want_dict == food_dict:
            answer += 1
    
    return answer
