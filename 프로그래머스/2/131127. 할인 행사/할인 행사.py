from collections import defaultdict

def solution(want, number, discount):
    possible = 0  # 가능한 날
    want_dict = defaultdict(int)  # (사야하는 물건: 수량) 딕셔너리
    discount_dict = defaultdict(int)  # n일동안 할인하는 물건 딕셔너리
    
    # 딕셔너리에 저장
    for goods, count in zip(want, number):
        want_dict[goods] = count
    
    # 할인 물건 딕셔너리 초기화
    for i in range(sn := sum(number)):
        discount_dict[discount[i]] += 1
    
    s, e = 0, sn-1  # 시작, 끝
    
    while e < len(discount)-1:
        if want_dict == discount_dict:
            possible += 1
            
        discount_dict[discount[s]] -= 1
        
        if discount_dict[discount[s]] == 0:
            del discount_dict[discount[s]]
            
        s += 1
        e += 1
        
        discount_dict[discount[e]] += 1
    
    if want_dict == discount_dict:
        possible += 1
    
    return possible