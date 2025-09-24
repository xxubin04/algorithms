def solution(wallet, bill):
    answer = 0
    
    if wallet[0] > wallet[1]:
        wallet[0], wallet[1] = wallet[1], wallet[0]
        
    if bill[0] > bill[1]:
        bill[0], bill[1] = bill[1], bill[0]
    
    while not (bill[0] <= wallet[0] and bill[1] <= wallet[1]):
        bill[1] //= 2
        answer += 1
        
        if bill[0] > bill[1]:
            bill[0], bill[1] = bill[1], bill[0]
    
    return answer