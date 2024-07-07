"""

의상

[의상명, 의상종류] 들을 줌
종류별로 최대 하나씩만 입을 수 있음.
안입을 수는 있지만, 최소 한개는 입어야함.
경우의수?

어차피 의상명 안겹치니깐 Counter 쓰는게 나을듯.

reduce를 쓸 수도 있는데 왜냐면 다 곱해야하니깐
for문이 더 깔끔한 느낌이여서 굳이라는 생각이 드네요

"""

from collections import Counter as cnter


def solution(clothes):
    Cnter = cnter(zip(*clothes)[1])
    Result = 1
    for Cnt in Cnter.values():
        Result *= Cnt + 1

    return Result - 1
