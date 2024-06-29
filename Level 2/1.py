"""

최댓값과 최솟값

"1 2 3 4" -> "1 4"

"""


def solution(s):
    tuple1 = tuple(map(int, s.split(" ")))
    return f"{min(tuple1)} {max(tuple1)}"
