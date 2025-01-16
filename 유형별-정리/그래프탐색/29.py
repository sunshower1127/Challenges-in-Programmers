"""피로도

최대한 많이 던전 탐색

k = 현재피로도
dungeons = [[최소 필요 피로도, 소모 피로도]]

어떤 애부터 방문해야하는지 고려해야하고,
경로의 최대값을 찾아내야하기때문에
dfs 굳이 안써도 됨.

---
2회차
bool[] 은 비트연산으로 바꿀 수 있다. 파이썬에선 무적임.

"""

from collections import deque


def solution(k, dungeons):
    result = 0

    q = deque()
    q.append((k, 0))
    while q:
        fatigue, visited = q.popleft()

        cnt = 0
        for i, dungeon in enumerate(dungeons):
            if visited & 1 << i:
                continue
            if fatigue < dungeon[0]:
                continue

            cnt += 1
            q.append((fatigue - dungeon[1], visited | 1 << i))

        if cnt == 0:
            result = max(result, bin(visited).count("1"))

    return result
