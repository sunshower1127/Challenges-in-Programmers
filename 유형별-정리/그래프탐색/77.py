"""거리두기 확인하기

맨해튼 거리가 2이하인 애 찾아내기.
어떤 애가 있으면 선택해서 2만큼 전진 시켜보기.
각자 그냥 탐색하다가 어 P가 있어? 그럼 바로 return 0

확실히 함수로 끊어서 return 처리하는게 중요한 문제였음.
"""

from collections import deque


def alert(sy, sx, place):
    q = deque()
    q.append((sy, sx, 0))

    visited = [[False] * 5 for _ in range(5)]
    visited[sy][sx] = True

    DY = [1, 0, -1, 0]
    DX = [0, 1, 0, -1]

    while q:
        y, x, dist = q.popleft()

        if dist == 2:
            continue

        for dy, dx in zip(DY, DX):
            ny, nx = y + dy, x + dx

            if not (0 <= ny < 5 and 0 <= nx < 5):
                continue
            if visited[ny][nx]:
                continue
            if place[ny][nx] == "X":
                continue
            if place[ny][nx] == "P":
                return True

            q.append((ny, nx, dist + 1))
            visited[ny][nx] = True

    return False


def search_place(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == "P":
                if alert(y, x, place):
                    return 0

    return 1


def solution(places):
    return [search_place(place) for place in places]
