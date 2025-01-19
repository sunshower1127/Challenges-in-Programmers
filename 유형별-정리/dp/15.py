"""멀리 뛰기

1칸 또는 2칸 뛸 수 있을 때, n칸을 뛰는 방법의 수

전형적인 dp 문제

"""


def solution(n):
    Dp = [0] * (n + 1)
    Dp[:2] = 1, 1

    for i in range(2, n + 1):
        Dp[i] = (Dp[i - 1] + Dp[i - 2]) % 1234567

    return Dp[n]
