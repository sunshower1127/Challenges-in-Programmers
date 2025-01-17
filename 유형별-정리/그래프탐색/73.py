"""미로 탈출
최소시간 -> bfs

첫번째 목표 -> 레버 당기기
두번째 목표 -> 도착지점 가기

분리해서 구하면 됨.
"""

from collections import deque


def get_dist(sy, sx, arrive_symbol, maps, height, width):
    visited = [[False] * width for _ in range(height)]

    q = deque()
    q.append((sy, sx, 0))
    visited[sy][sx] = True

    DY = [1, 0, -1, 0]
    DX = [0, 1, 0, -1]
    while q:
        y, x, dist = q.popleft()

        for dy, dx in zip(DY, DX):
            ny, nx = y + dy, x + dx

            if not (0 <= ny < height and 0 <= nx < width):
                continue
            if visited[ny][nx]:
                continue
            if maps[ny][nx] == "X":
                continue

            if maps[ny][nx] == arrive_symbol:
                return dist + 1

            visited[ny][nx] = True
            q.append((ny, nx, dist + 1))

    return 0


def solution(maps):
    height = len(maps)
    width = len(maps[0])

    for y in range(height):
        for x in range(width):
            if maps[y][x] == "S":
                sy, sx = y, x
            if maps[y][x] == "L":
                ly, lx = y, x

    dist_s_to_l = get_dist(sy, sx, "L", maps, height, width)
    if not dist_s_to_l:
        return -1

    dist_l_to_e = get_dist(ly, lx, "E", maps, height, width)
    if not dist_l_to_e:
        return -1

    return dist_s_to_l + dist_l_to_e
