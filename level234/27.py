"""거스름돈

인데 1 2 5원임.

dp 아닌가욥

   1  2  3  4  5
1  1  1  1  1  1
2  1  2  2  3  3
5
"""


def solution(n, money):
    height = len(money)
    dp = [[0] * (n + 1) for _ in range(height + 1)]

    for y in range(height + 1):
        dp[y][0] = 1

    for y, coin in enumerate(money, 1):
        for x in range(1, n + 1):
            if x < coin:
                dp[y][x] = dp[y - 1][x]
            else:
                dp[y][x] = dp[y - 1][x] + dp[y][x - coin]

    return dp[height][n]
