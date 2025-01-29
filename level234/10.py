"""기지국 설치

2*10^8
흠... n까지는 허용 아닌가 근데

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
            - - o  -  -

"""

import math


def solution(n, stations, w):
    old_station = -w
    stations.append(n + w + 1)
    cnt = 0

    for station in stations:
        dist = station - old_station - 2 * w - 1

        old_station = station
        if dist <= 0:
            continue

        cnt += math.ceil(dist / (2 * w + 1))

    return cnt
