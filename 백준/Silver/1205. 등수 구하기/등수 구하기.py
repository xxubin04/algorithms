input = open(0).readline

N, t_score, P = map(int, input().split())

if N == 0:
    print(1)
    exit()
else:
    scores = sorted(list(map(int, input().split())), reverse=True)

if t_score in scores:
    for i in range(N):
        if scores[i] < t_score:
            print(scores.index(t_score) + 1)
            exit()
        elif i == N-1 and scores[N-1] == t_score:
            if N >= P:
                print(-1)
            else:
                print(scores.index(t_score) + 1)
                exit()
else:
    for i in range(N):
        if scores[i] < t_score and i <= P:
            print(i+1)
            exit()
    if N < P:
        print(N+1)
        exit()
    print(-1)