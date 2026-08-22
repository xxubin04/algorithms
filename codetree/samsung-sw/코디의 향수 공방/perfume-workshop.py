scent_dict = {}  # 향도들의 딕셔너리 (향료 번호: 향도)


## 2. 향료 추가(v)
def add_scent(n):
    global N, scent_dict

    N += 1  # 마지막 향료의 번호 1 증가
    scent_dict[N] = n  # 향료 추가


## 3. 향료 폐기(idx)
def remove_scent(i):
    global scent_dict

    # 아직 i번 향료가 존재한다면, 폐기 + 출력
    if i in scent_dict:
        print(scent_dict[i])
        scent_dict.pop(i)
    else:  # i번 향료가 이미 폐기/존재하지 않는다면, -1 출력
        print(-1)


## 4. 블렌딩(K)
def blending(k):
    global av_scents, scent_dict

    dp = [0] + [float('inf')] * k

    for v in av_scents:
        for x in range(0, k + 1):
            if x >= v:
                dp[x] = min(dp[x], dp[x - v] + 1)

    if dp[k] == float('inf'):
        return -1

    return dp[k]


## 5. 향수 구성(K)
def make_perfume(k):
    case = 0  # 경우의 수

    if len(av_scents) == 0:  # 남은 향료가 아무것도 없다면
        return 0

    suffix, ma = suffix_sum(k)  # 뒤쪽 누적합으로 미리 각 인덱스 이상의 향료 개수 세어두기

    for a in scent_dict.values():
        for b in scent_dict.values():
            c = k - a - b  # c보다 크거나 같은 값 개수 찾기 (c >= k - a - b)

            if c <= 1:  # c가 1 이하면, 세 번째 향료가 무엇이든 조건 만족
                case += len(av_scents)
            elif c > ma:  # c가 ma(가장 큰 향도)보다 크다면 k 이상인 합이 없으므로 넘어감
                continue
            else:
                case += suffix[c]  # c 이상인 향료의 개수만큼 더하기

    return case


## 5-1. 뒤쪽 누적합
def suffix_sum(k):
    suffix = [0] * ((ma := av_scents[-1]) + 2)
    freq = [0] * (ma + 1)

    for v in av_scents:  # 향도 개수 세어두기
        freq[v] += 1

    for x in range(ma, 0, -1):
        suffix[x] = freq[x] + suffix[x + 1]

    return suffix, ma


# ## 5-1. 이진탐색
# def binary_search(s, e, c):
#     if s > e:
#         return s

#     mid = (s + e) // 2

#     if av_scents[mid] >= c:
#         return binary_search(s, mid - 1, c)
#     else:
#         return binary_search(mid + 1, e, c)


for q in range(Q := int(input())):

    ## 1. 향료 준비
    if q == 0:  # 첫 번째 단계라면
        inp = list(map(int, input().split()))  # 작업 정보를 리스트로 입력받음
        _, N, scents = inp[0], inp[1], inp[2:]  # 마지막 향료의 번호 N, 향도들의 리스트 scents
        for s in range(N):
            scent_dict[s + 1] = scents[s]  # (향료 번호: 향도) 저장
        continue

    # 두 번째 이상의 단계라면
    cmd, num = map(int, input().split())  # 작업번호, 숫자(v, idx, K)

    if cmd == 2:
        add_scent(num)
    elif cmd == 3:
        remove_scent(num)
    elif cmd == 4:
        av_scents = sorted(list(scent_dict.values()))  # 향도들의 리스트 (오름차순 정렬)
        print(blending(num))
    elif cmd == 5:
        av_scents = sorted(list(scent_dict.values()))
        print(make_perfume(num))
