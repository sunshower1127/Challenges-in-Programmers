"""등굣길

dp문제임
오랜만에 풀어보네요

"""


def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    is_puddle = [[False] * (m + 1) for _ in range(n + 1)]

    for x, y in puddles:
        is_puddle[y][x] = True

    dp[0][1] = 1

    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if is_puddle[y][x]:
                continue

            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % 1_000_000_007

    return dp[n][m]
