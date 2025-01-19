"""의상
각 종류별로 최대 1가지
완전 똑같지만 않으면됨.

그래도 최소 1개는 입어야함.

X12
해서 의상 종류별 +1 한다음에 모두 곱하고,
아예 안입는 경우만 빼면 될듯


"""

from collections import defaultdict
from functools import reduce
from operator import mul


def solution(clothes):
    items = defaultdict(set)

    for name, category in clothes:
        items[category].add(name)

    return reduce(mul, (len(v) + 1 for v in items.values())) - 1
