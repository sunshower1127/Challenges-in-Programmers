"""정수 삼각형
0 0 0 0 0 0
0 7
0 3 8

사실 뭐 dp는 너무 마스터를 해버려서
"""


def solution(triangle):
    N = len(triangle)
    dp = [0] * (N + 1)

    for y in range(N):
        for x in reversed(range(1, y + 2)):
            dp[x] = max(dp[x], dp[x - 1]) + triangle[y][x - 1]

    return max(dp)
