"""H-Index
h: 값이 h이상인 논문이 h편이상
0부터 시작되는거임

논문은 1000개.
값이 100000
10^9면 아슬아슬하게 세이프 아니냐
정렬만 해주면 괜찮을듯

결론적으로 카운터는 안써도 됐네. 그냥 구현문제임.
"""

from collections import Counter


def solution(citations):
    cnter = Counter(citations)
    num = 0
    for h in range(max(citations), -1, -1):
        if h in cnter:
            num += cnter[h]
        if h <= num:
            return h
