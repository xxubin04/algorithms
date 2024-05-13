input = open(0).readline

for _ in range(int(input())):
    times = list(input().split())
    time_sorted = {}
    
    for idx, t in enumerate(times):
        hh, mm = map(int, t.split(':'))
        h_degree = (hh % 12) * 30 + mm / 2  
        m_degree = mm * 6  
        degree = abs(h_degree - m_degree) 
        if degree > 180:
            degree = 360 - degree
        time_sorted[idx] = degree
    sorted_times = sorted(times, key=lambda x: (time_sorted[times.index(x)], x))
    print(sorted_times[2])
