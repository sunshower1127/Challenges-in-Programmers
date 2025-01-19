"""하노이의 탑

어떤 식으로 확장될 수 있는가?

일단 기둥은 3개 고정에
원판이 늘어남

2개 -> 위에있는걸 가운데에, 아래있는걸 3에, 다시 올리기

3개 ->

n-1개를 2에 옮기고, 마지막 한개를 3에 옮기고, 나머지를 3에 옮기면 됨.

근데 이건 dp가 아니라 그냥 분할정복인데?

"""


def solution(n):
    result = []

    def move(n, start, end):
        if n == 1:
            result.append([start, end])
            return
        rest = next(iter({1, 2, 3} - {start, end}))
        move(n - 1, start, rest)
        result.append([start, end])
        move(n - 1, rest, end)

    move(n, 1, 3)
    return result
