# def solution(genres, plays):
#     answer = []
#     genre_dict = {}
#     genre_sum = {}
    
#     for idx in range(len(genres)):
#         if (g := genres[idx]) in genre_dict:
#             genre_dict[g].append((idx, (p := plays[idx])))
#             genre_sum[g] += p
#         else:
#             genre_dict[g] = [(idx, (p := plays[idx]))]
#             genre_sum[g] = p
    
#     genre_sum = sorted(genre_sum.items(), key=lambda x: x[1], reverse=True)

#     for k in genre_sum:
#         genre_dict[k[0]] = sorted(genre_dict[k[0]], key=lambda x: x[1], reverse=True)
#         answer.append(genre_dict[k[0]][0][0])
#         if len(genre_dict[k[0]]) >= 2:
#             answer.append(genre_dict[k[0]][1][0])
    
#     return answer



from collections import defaultdict

def solution(genres, plays):
    answer = []

    genre_songs = defaultdict(list)
    genre_total = defaultdict(int)

    # 장르별 곡 정보와 총 재생 횟수 저장
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_songs[genre].append((idx, play))
        genre_total[genre] += play
        
    # 총 재생 횟수가 많은 장르부터
    genre_order = sorted(genre_total, key=lambda genre: genre_total[genre], reverse=True)

    for genre in genre_order:
        genre_songs[genre].sort(key=lambda x: (-x[1], x[0]))

        # 장르별 최대 2곡
        for idx, play in genre_songs[genre][:2]:
            answer.append(idx)

    return answer