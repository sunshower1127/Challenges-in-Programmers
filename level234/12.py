"""스티커 모으기(2)

100 000개

최대값이라...
음...
근데 뜯으면 옆에거 못뜯음

원형임 게다가

그냥 일단 제일 큰거 뜯는게 맞지 않나
라고할뻔이네요
절대 아니고

하나하나 뜯어본다?

모르겠는데? 전혀?

원형 DP라고 하네요 레전드

1. 일단 원형이라고 생각하지 말고 DP로 풀고
2. 원형일때를 고려해서 덧붙여주면됨(index가 0일때만 유의하면 될듯)
"""


def solution(sticker):
    N = len(sticker)

    if N <= 2:
        return max(sticker)

    # 첫번째 인덱스 선택 X
    dp = [0] * N
    dp[1] = sticker[1]
    for n in range(2, N):
        dp[n] = max(dp[n - 2] + sticker[n], dp[n - 1])

    max_v = dp[N - 1]

    # 첫번째 인덱스 선택

    dp = [0] * (N - 1)
    dp[0] = sticker[0]
    dp[1] = max(dp[0], sticker[1])
    for n in range(2, N - 1):
        dp[n] = max(dp[n - 2] + sticker[n], dp[n - 1])

    max_v = max(max_v, dp[N - 2])

    return max_v
