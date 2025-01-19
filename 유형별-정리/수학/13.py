"""N개의 최소공배수

음 잘 참고하도록 하자
"""

from functools import reduce
from math import gcd


def lcm(*args):
    return reduce(lambda x, y: x * y // gcd(x, y), args)


def solution(arr):
    return lcm(*arr)
