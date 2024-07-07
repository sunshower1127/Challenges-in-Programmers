"""

점프와 순간 이동

n칸 앞으로 점프 -> n만큼 에너지 소모

n -> 2n 순간이동 -> 에너지 소모 x

에너지 최솟값 계산

tip : 반대로 생각해보자. 곱하기 -> 나누기

"""


def solution(n):
    Sum = 0
    while n != 0:
        n, r = divmod(n, 2)
        Sum += r

    return Sum
