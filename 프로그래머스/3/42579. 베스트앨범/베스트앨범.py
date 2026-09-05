def solution(genres, plays):
    answer = []
    genre_dict = {}
    genre_sum = {}
    
    for idx in range(len(genres)):
        if (g := genres[idx]) in genre_dict:
            genre_dict[g].append((idx, (p := plays[idx])))
            genre_sum[g] += p
        else:
            genre_dict[g] = [(idx, (p := plays[idx]))]
            genre_sum[g] = p
    
    genre_sum = sorted(genre_sum.items(), key=lambda x: x[1], reverse=True)

    for k in genre_sum:
        genre_dict[k[0]] = sorted(genre_dict[k[0]], key=lambda x: x[1], reverse=True)
        answer.append(genre_dict[k[0]][0][0])
        if len(genre_dict[k[0]]) >= 2:
            answer.append(genre_dict[k[0]][1][0])
    
    return answer