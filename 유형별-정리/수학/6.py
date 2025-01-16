"""

숫자의 표현

15 = 15
15 = 7 + 8
15 = 4 + 5 + 6
15 = 1 + 2 + 3 + 4 + 5

연속된 수의 합으로 표현 할 수 있는 개수 -> 4

tip : 연속된 수의 합은 가우스 합으로 풀 수 있음 -> 시간복잡도 단축

"""


def solution(n):
    Cnt = 0

    def sum1(x, y):
        return (x + y) * (y - x + 1) // 2

    # sum1 = lambda x, y: (x + y) * (y - x + 1) // 2

    for Begin in range(1, n + 1):
        for End in range(Begin, n + 1):
            if sum1(Begin, End) == n:
                Cnt += 1
            elif sum1(Begin, End) > n:
                break
    return Cnt
