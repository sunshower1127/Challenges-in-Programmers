"""땅따먹기

range를 set에다 넣기 -> {*range(4)}
그냥 아이템 하나 set에다 넣기 -> {x}
"""


def solution(land):
    height = len(land)
    width = len(land[0])
    dp = land[0][:]

    for y in range(1, height):
        new = [0] * 4
        for x in range(width):
            new[x] = land[y][x] + max(dp[ox] for ox in ({*range(4)} - {x}))

        dp = new

    return max(dp)
