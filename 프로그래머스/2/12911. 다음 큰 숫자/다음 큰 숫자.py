def solution(n):
    bin_n = format(n, 'b')  # n을 이진변환 
    cnt_n = bin_n.count('1')
    
    nn = n
    while True:
        nn += 1
        bin_nn = format(nn, 'b')
        if (cnt_nn := bin_nn.count('1')) == cnt_n:
            return nn
    
    return