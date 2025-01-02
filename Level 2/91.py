"""두 원 사이의 정수 쌍

세세한 디테일(floor, ceil) (예외처리등..)이 필요한 문제였음
"""

import math


def solution(r1, r2):
    cnt = 0

    def get_y(r, x):
        return max(0, (r**2 - x**2)) ** 0.5

    for x in range(r2 + 1):  # 0 1 2 3
        y2 = math.floor(get_y(r2, x))
        y1 = math.ceil(get_y(r1, x))
        cnt += (y2 - y1 + 1) * 2

    n = 4
    cnt *= 2
    cnt -= n * (r2 - r1 + 1)
    return cnt
