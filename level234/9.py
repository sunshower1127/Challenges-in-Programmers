"""단속카메라

저번에 푼 문제인데도 어렵네요

-
--
 --
---

-
--
---
 --

끝점 기준으로 정렬하고,
카메라가 이 차를 만났는지 못만났는지 판단하면서
못만났으면 cnt += 1

진짜 이해 못하겠음 이 알고리즘은
"""


def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = -30001
    cnt = 0

    for start, end in routes:
        if start > camera:
            cnt += 1
            camera = end

    return cnt
