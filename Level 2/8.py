"""

피보나치 수

F(n) = F(n-1) + F(n-2) (n >= 2)
F(0) = 0, F(1) = 1

"""


def solution(n):
    N = n
    dp = [0] * (N + 1)
    dp[:2] = 0, 1

    for n in range(2, N + 1):
        dp[N] = dp[n - 2] + dp[n - 1]
        dp[n] %= 1234567

    return dp[-1]
