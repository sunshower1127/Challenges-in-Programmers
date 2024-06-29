"""

귤 고르기

k개를 고르는데, 최대한 중복되는 숫자가 많게 고르자.
-> 숫자 종류의 최솟값을 리턴

tip : 종류별로 개수를 세는 Counter를 사용하면 편하다.

"""

from collections import Counter


def solution(k, tangerine):
    counter = Counter(tangerine)
    cnt = 0
    for value in sorted(counter.values(), reverse=True):
        k -= value
        if k <= 0:
            cnt += 1
            break
        cnt += 1

    return cnt
