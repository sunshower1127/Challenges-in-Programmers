"""최댓값과 최솟값

"1 2 3 4" -> "1 4"

"""


def solution(s):
    Tuple = tuple(map(int, s.split(" ")))
    return f"{min(Tuple)} {max(Tuple)}"
