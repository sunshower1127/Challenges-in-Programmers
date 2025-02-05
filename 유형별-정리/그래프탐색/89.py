"""N-Queen
경우의 수 -> dfs -> 재귀함수
그냥 외우자

이상한 문제야.. x in path 안쓰면 시간초과라니..
"""


def solution(n):
    path = []
    cnt = 0

    def dfs():
        nonlocal cnt

        y = len(path)

        if y == n:
            cnt += 1
            return

        for x in range(n):
            if any(x == px or abs(y - py) == abs(x - px) for py, px in enumerate(path)):
                continue

            path.append(x)
            dfs()
            path.pop()

    dfs()
    return cnt
