"""멀쩡한 사각형
일단 가로와 세로의 최대 공약수
가로 * 세로  - (가로 + 세로 - 최대 공약수)

뭐야 이게 되네

근데 최소공배수, 최대공약수 이거 이름 외우는게 쉽지 않네요
greatest common divisor -> 최대 공 약수
least common multiple -> 최소 공 배수
"""

import math


def solution(w, h):
    return w * h - (w + h - math.gcd(w, h))
