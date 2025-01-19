"""귤 고르기

귤 k개를 고를거임. 이때 어떤 걸 빼야 최소종류가 나옴?

"""

from collections import Counter


def solution(k, tangerine):
    cnter = Counter(tangerine)
    cnts = sorted(cnter.values())
    n = len(tangerine) - k

    for i in range(len(cnts)):
        n -= cnts[i]
        if n < 0:
            return len(cnts) - i
