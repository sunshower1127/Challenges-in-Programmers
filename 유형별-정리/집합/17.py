"""

귤 고르기

k개를 고르는데, 최대한 중복되는 숫자가 많게 고르자.
-> 숫자 종류의 최솟값을 리턴

tip : 종류별로 개수를 세는 Counter를 사용하면 편하다.

"""

from collections import Counter as cnter


def solution(k, tangerine):
    Cnter = cnter(tangerine)
    Cnt = 0
    for Value in sorted(Cnter.values(), reverse=True):
        k -= Value
        if k <= 0:
            Cnt += 1
            break
        Cnt += 1

    return Cnt
