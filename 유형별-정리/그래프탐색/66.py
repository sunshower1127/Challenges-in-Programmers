"""메뉴 리뉴얼

메뉴에서 공통점을 뽑아낸다라..
그냥 뽑아내면 될거갈은데
메모이제이션이 되나?

아하 sorted 리턴형은 list네요

"""

from collections import Counter
from itertools import combinations


def solution(orders, course):
    result = []
    for num in course:
        cnter = Counter()

        for order in orders:
            for comb in combinations(order, num):
                string = "".join(sorted(comb))
                cnter[string] += 1

        sorted_items = sorted(cnter.items(), reverse=True, key=lambda x: x[1])
        if not sorted_items:
            continue

        max_cnt = sorted_items[0][1]
        if max_cnt == 1:
            continue

        for name, cnt in sorted_items:
            if cnt != max_cnt:
                break
            result.append(name)

    result.sort()
    return result
