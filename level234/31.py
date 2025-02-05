"""도둑질

인접한 두 집을 털면 안될때 최댓값..

그냥 일자면
이 집을 털었을때 / 안털었을때


oxo
oxxo
이 두가지 경우밖에 없으니깐

dp[n] = max(dp[n-2], dp[n-3]) + money[n]

하고
answer = max(dp[-2:])
인데

원형이란 말이죠

xo|x
x|

이렇게 스타트가 두개로 나뉘겠죠

음.

그냥 외워
반드시 마지막꺼를 선택하지 않아도 된다면
압축이 가능하다

"""


def get_max(money):
    N = len(money)
    if N == 0:
        return 0
    if N == 1:
        return money[0]

    dp = [0] * (N + 1)
    dp[1] = money[0]

    for n in range(2, N + 1):
        dp[n] = max(dp[n - 1], dp[n - 2] + money[n - 1])

    return dp[-1]


def solution(money):
    return max(get_max(money[:-1]), get_max(money[1:-2]) + money[-1])
