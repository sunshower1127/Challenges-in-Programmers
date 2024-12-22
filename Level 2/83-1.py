"""광물 캐기

곡괭이는 5개 광물을 캐야함. 그리고 버림.

피로도의 최솟값을 구해야함.

그냥 돌일 수록 그냥 돌 곡괭이로 캐는게 낫고

다이아몬드일수록 비싼 곡괭이로 캐는게 낫다 이거임

5개씩이니깐 5개로 묶을 수 있고


이게 선형적이니깐 dp가 맞는거 같기도 한데

다 못캘 수도 있는거라 이게 값을 예측해서 배분하는것도 쉽지않고

15! / 5! / 5! / 5! -> 14 13 3 11 2 9 7 -> 14 13 11 9 7 6 -> 10^6 정도

되네

그냥 브루트네요 뭐 없음

브루트 구현을 못하겠음

오류가 났는데, 그냥 코드 하나하나 잘 읽어보면 됐었음. 너무 좌절할 필요는 없을듯.


tip: 재귀 함수에서 결과를 저장하는 전역변수를 쓰는대신 yield로 대체 가능하다.
"""

import math


def getcombs(ls, picks, n):
    if n == -1 or sum(picks) == 0:
        yield ls
        return

    if picks[0]:
        newpicks = picks[:]
        newpicks[0] -= 1
        yield from getcombs([*ls, "diamond"], newpicks, n - 1)

    if picks[1]:
        newpicks = picks[:]
        newpicks[1] -= 1
        yield from getcombs([*ls, "iron"], newpicks, n - 1)

    if picks[2]:
        newpicks = picks[:]
        newpicks[2] -= 1
        yield from getcombs([*ls, "stone"], newpicks, n - 1)


tirement = {
    "diamond": {"diamond": 1, "iron": 1, "stone": 1},
    "iron": {"diamond": 5, "iron": 1, "stone": 1},
    "stone": {"diamond": 25, "iron": 5, "stone": 1},
}


def solution(picks, minerals):
    N = math.ceil(len(minerals) / 5)

    min_v = float("INF")
    for comb in getcombs([], picks, N):
        v = sum(
            tirement[comb[i // 5]][mineral]
            for i, mineral in enumerate(minerals)
            if i // 5 < sum(picks)
        )
        min_v = min(min_v, v)

    return min_v
