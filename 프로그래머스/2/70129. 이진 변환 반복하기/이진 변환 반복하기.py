def solution(s):
    result = [0, 0]  # 변환 횟수, 제거된 0의 개수 

    while s != '1':
        result[1] += len(s) - (sc := s.count('1'))  # 제거한 0의 개수
        s = format(sc, 'b')  # 이진수로 변환하면서 접두사 '0b' 제거
        result[0] += 1
    
    return result
        