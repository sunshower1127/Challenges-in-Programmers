"""[PCCE 기출문제] 10번 / 공원

이지하죠
정사각형 크기 구하는건 너무 많이 해서

"""


def solution(mats, park):
    mats.sort(reverse=True)
    height = len(park)
    width = len(park[0])
    dp = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            if park[y][x] == "-1":
                dp[y][x] = min(dp[y - 1][x], dp[y - 1][x - 1], dp[y][x - 1]) + 1

    max_v = max(map(max, dp))

    for v in mats:
        if v > max_v:
            continue

        return v

    return -1
