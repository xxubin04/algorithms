from itertools import product

def solution(users, emoticons):
    service = 0  # 서비스 가입자 수
    sales = 0  # 매출액
    
    for discounts in product([10, 20, 30, 40], repeat=len(emoticons)):
        tservice = 0  # 이번 할인율에서의 서비스 가입자 수
        tsales = 0  # 이번 할인율에서의 매출액 
        
        for udiscnt, ustd in users:  # 사람들 각각 (사람들마다 할인율, 금액기준)
            ucal = 0  # 사람 1명의 구매액
                
            for idx in range(len(emoticons)):  # 이모티콘 각각 
                if discounts[idx] >= udiscnt:  # 이모티콘의 할인율이 더 클 때만 
                    ucal += emoticons[idx] * (100 - discounts[idx]) // 100  # 각 이모티콘의 가격
            
            if ucal >= ustd:  # 사람의 기준보다 매출액이 크거나 같으면, 서비스 가입
                tservice += 1
            else:  # 사람의 기준보다 매출액이 작으면, 그냥 구매
                tsales += ucal

        if tservice > service:  # 서비스 가입자 수가 이번 할인율 때 더 많다면
            service = tservice
            sales = tsales
        elif tservice == service:  # 서비스 가입자 수가 이번 할인율 때 같다면
            sales = max(sales, tsales)  # 더 큰 매출액으로 갱신

    return [service, sales]