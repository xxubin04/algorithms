r, c, k = map(int, input().split())  # 행, 열, 목표 숫자
graph = []

for _ in range(3):
    graph.append(list(map(int, input().split())))

# 1. 행 기준 출현 빈도 수 계산 
def cal_freq_row(row):
    freq_list = {}  # {숫자: 빈도 수}

    for i in graph[row]:
        if not i in freq_list.keys() and i != 0:  # 딕셔너리에 저장되어 있지 않다면
            freq_list[i] = 1
        elif i != 0:
            freq_list[i] += 1

    return freq_list

# 2. 열 기준 출현 빈도 수 계산
def cal_freq_col(col):
    freq_list = {}  # {숫자: 빈도 수}

    for row in graph:
        # print(f"row: {row}, col: {col}")
        if not (n := row[col]) in freq_list.keys() and n != 0:
            freq_list[n] = 1
        elif n != 0:
            freq_list[n] += 1

    return freq_list

# 3. 숫자 작은 순서대로 정렬
def align_ascend(f_list):
    f_list = dict(sorted(f_list.items(), key=lambda x: (x[1], x[0])))  # 빈도 수가 같으면 숫자가 작은 순서대로 정렬 
    
    return f_list

# 4. 행 정렬
def align_row(f_list, row):
    g_list = []
    for k, f in f_list.items():
        g_list.append(k)
        g_list.append(f)
    
    graph[row] = g_list

# 5. 열 정렬 
def align_col(f_list, col):
    g_list = []
    for k, f in f_list.items():
        g_list.append(k)
        g_list.append(f)
    
    for i in range(len(g_list)):
        if i >= len(graph):
            graph.append([])

        if len(graph[i]) <= col:
            graph[i].extend([0] * (col + 1 - len(graph[i])))

        graph[i][col] = g_list[i]
    
    for i in range(len(g_list), len(graph)):
        graph[i][col] = 0

# 6. 0으로 패딩
def padding():
    max_r = max(len(r) for r in graph)  # 최대 행 길이 
    
    for i in range(len(graph)):
        if (l := len(graph[i])) < max_r:
            for _ in range(max_r - l):
                graph[i].append(0)
    
    return

# 7. 100개 제외하고 버림
def del_100():
    # 행 길이 확인
    if len(graph[0]) > 100:
        for i in range(len(graph)):
            graph[i] = graph[i][:100]
    
    # 열 길이 확인 
    if len(graph) > 100:
        if (max_c := len(graph)) > 100:
            del graph[100:]

    return

# 8. 원하는 값인지 확인
def check_num():
    num_row = len(graph)
    num_col = len(graph[0])

    if num_row < r or num_col < c:
        return False

    if graph[r-1][c-1] == k:
        return True
    
    return False

cnt = 0

while True:
    if check_num():
        print(cnt)
        break

    if cnt == 100:
        print(-1)
        break

    cnt += 1

    num_row = len(graph)
    num_col = 0
    for j in range(len(graph)):
        if (l := len(graph[j])) > num_col:
            num_col = l

    if num_row >= num_col:
        for i in range(num_row):
            a = align_ascend(cal_freq_row(i))
            align_row(a, i)
            padding()
    else:
        for i in range(num_col):
            a = align_ascend(cal_freq_col(i))
            align_col(a, i)
            padding()

    padding()
    del_100()
