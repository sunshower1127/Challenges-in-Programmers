"""3 x n 타일링

아직 김선우 안죽었는지 한번 봅시다

2개 단위로 했었어야했나

2개 단위하고 4개 단위가 있어요

2개 단위는 3개
4개 단위는 2개

dp 이-지
중요한건 꺾이지 않는 디버깅 -> 중꺾디

"""


def solution(N):
    dp = [0] * (N + 1)
    dp[:4] = [1, 0, 3, 0]
    for n in range(4, N + 1):
        dp[n] = (3 * dp[n - 2] + 2 * sum(dp[n - 4 : 0 : -2]) + 2) % 1_000_000_007

    return dp[N]
