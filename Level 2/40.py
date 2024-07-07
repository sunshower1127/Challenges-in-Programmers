"""

땅따먹기

N행 4열 맵

행에서 하나만 밟아서 쭉 내려왔을때 합의 최고 점수 구하기

-> 전형적인 dp 문제.


"""


def solution(land):

    Dp = land[0][:]

    for i in range(1, len(land)):
        New = [0] * 4
        New[0] = max(Dp[1], Dp[2], Dp[3]) + land[i][0]
        New[1] = max(Dp[0], Dp[2], Dp[3]) + land[i][1]
        New[2] = max(Dp[0], Dp[1], Dp[3]) + land[i][2]
        New[3] = max(Dp[0], Dp[1], Dp[2]) + land[i][3]

        Dp = New

    return max(Dp)
