"""

H-Index

[3, 0, 6, 1, 5] 논문의 인용횟수들 배열이 있음.

h번 이상인 값이 h개 이상인 h의 최댓값을 구하라.

[0, 1, 3, 5, 6] 이므로, 답은 3이됨.

tip : 뭔가 머리아픈 이런게 나오면 그냥 주어진대로 계산하자. 시간복잡도도 높지않고.

"""


def solution(citations):
    citations.sort()
    N = len(citations)
    for i in range(N):
        if citations[i] >= N - i:
            return N - i
    return 0
