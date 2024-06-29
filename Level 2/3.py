"""

최솟값 만들기

[1,2] [3,4] -> 1*4 + 2*3 = 10
해서 10인 최솟값 만드는거임.

tip : 넓이 관점은 정렬이 답인 경우가 많음

"""


def solution(A, B):
    A.sort()
    B.sort(reverse=True)
    return sum([a * b for a, b in zip(A, B)])
