"""베스트 앨범

장르
    노래
        고유번호


노래를 주는데
음 그렇대요

그냥 쉬운 문제였음
"""

from collections import defaultdict


def solution(genres, plays):
    data = defaultdict(list)

    for i, (genre, play_cnt) in enumerate(zip(genres, plays)):
        data[genre].append((play_cnt, i))

    genre_list = sorted(
        data.values(), key=lambda x: sum(play_cnt for play_cnt, _ in x), reverse=True
    )

    result = []

    for play_list in genre_list:
        play_list.sort(key=lambda x: x[0], reverse=True)
        result.append(play_list[0][1])
        if len(play_list) >= 2:
            result.append(play_list[1][1])

    return result
