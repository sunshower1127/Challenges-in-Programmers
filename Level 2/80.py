"""하노이의 탑
푸는법 모르니깐 대충 컨셉만 가져와봄
dp라는데요

중요한건 이제 푸는법을 쪼개보면

1. n-1개 원판을 가운데로 옮기고
2. n 원판을 1에서 3으로 옮기고
3. n-1개 원판을 3으로 옮긴다.

1번하고 3번은 같은 방법을 씀. 그리고 n-1하고 관련 있기 때문에 재귀적으로 접근할 수 있음.

출발 위치, 도착위치, n 을 받으면 될듯

옮기는 방법은 모두 같음.

수정사항

set((1, 2, 3)) -> {1, 2, 3} 으로 변경가능

set에서 그냥 하나만 가져오고 싶을때 : list(셋)[0] -> 셋.pop()

그리고 yield를 사용할 수 있음.
"""


def move(start, end, n):
    middle = {1, 2, 3} - {start, end}
    middle = middle.pop()
    if n == 1:
        return [[start, end]]

    return [*move(start, middle, n - 1), [start, end], *move(middle, end, n - 1)]


def solution(n):
    return move(1, 3, n)


# # yield 버전
# def move(start, end, n):
#     middle = {1, 2, 3} - {start, end}
#     middle = middle.pop()
#     if n == 1:
#         yield [start, end]
#     else:
#         yield from move(start, middle, n - 1)
#         yield [start, end]
#         yield from move(middle, end, n - 1)


# def solution(n):
#     return list(move(1, 3, n))
