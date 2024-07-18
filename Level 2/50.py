"""

2 x n 타일링

아 네... dp

"""


def solution(n):
    Dp = [0] * (n + 1)

    Dp[0] = 1
    Dp[1] = 1

    for i in range(2, n + 1):
        Dp[i] = (Dp[i - 1] + Dp[i - 2]) % 1000000007

    return Dp[n]
