"""야근 지수

제곱이 합이 최소가 되도록 하게 만들어라~

works는 20000임 길이가

흠

그냥 제일 긴 애부터 깎으면 될거 같은데
-> 맞았음.

"""

from heapq import heapify, heappop, heappush
from operator import neg


def solution(n, works):
    max_heap = list(map(neg, works))
    heapify(max_heap)

    while max_heap and n > 0:
        item = -heappop(max_heap)
        item -= 1
        n -= 1
        if item > 0:
            heappush(max_heap, -item)

    return sum(item**2 for item in max_heap)
