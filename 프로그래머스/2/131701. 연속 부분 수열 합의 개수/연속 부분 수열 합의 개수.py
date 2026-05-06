def solution(el):
    sums = set()
    for i in range(l := len(el)):
        st = 0
        for j in range(l):
            st += el[(i+j)%l]
            sums.add(st)
    
    return len(sums)