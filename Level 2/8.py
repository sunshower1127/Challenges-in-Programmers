"""

피보나치 수

F(n) = F(n-1) + F(n-2) (n >= 2)
F(0) = 0, F(1) = 1

"""


def solution(n):
    N = n
    Dp = [0] * (N + 1)
    Dp[:2] = 0, 1

    for n in range(2, N + 1):
        Dp[N] = Dp[n - 2] + Dp[n - 1]
        Dp[n] %= 1234567

    return Dp[-1]
