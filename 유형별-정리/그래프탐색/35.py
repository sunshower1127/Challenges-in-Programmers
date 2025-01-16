"""게임 맵 최단거리

전형적인 bfs

근데 디테일이 좀 많네요. 실수하기 좋을듯.

1. maps에서 1은 갈 수 있는 길, 0은 벽이다. (보통은 반대긴함)
2. maps를 계속해서 업데이트해줘야함.

"""

from collections import deque


def solution(maps):
    height = len(maps)
    width = len(maps[0])

    q = deque()
    q.append(((0, 0), 2))
    maps[0][0] = 2

    DY = [0, 1, 0, -1]
    DX = [1, 0, -1, 0]

    while q:
        (y, x), dist = q.popleft()

        for dy, dx in zip(DY, DX):
            ny = y + dy
            nx = x + dx

            if not (0 <= ny < height and 0 <= nx < width):
                continue
            if maps[ny][nx] != 1:
                continue
            if (ny, nx) == (height - 1, width - 1):
                return dist

            maps[ny][nx] = dist + 1
            q.append(((ny, nx), dist + 1))

    return -1
