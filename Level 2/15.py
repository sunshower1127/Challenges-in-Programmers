"""

멀리 뛰기

1칸 또는 2칸 뛸 수 있을 때, n칸을 뛰는 방법의 수

전형적인 dp 문제

"""


def solution(n):
    dp = [0] * (n + 1)
    dp[:2] = 1, 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567

    return dp[n]
