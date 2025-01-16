"""

게임 맵 최단거리

maps에서 0은 벽, 1은 길

(1,1)에서 출발해서 (n,m)까지 가는 최단거리 -> 없으면 -1

tip : 최단경로 -> bfs

"""

from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    DY = [1, 0, -1, 0]
    DX = [0, 1, 0, -1]

    Dist = [[0] * M for _ in range(N)]

    Queue = deque([(1, 1)])
    while Queue:
        y, x = Queue.popleft()

        for i in range(4):
            Ny = y + DY[i]
            Nx = x + DX[i]

            if not (1 <= Ny <= N) or not (1 <= Nx <= M):
                continue

            if maps[Ny - 1][Nx - 1] == 0:
                continue

            if Dist[Ny - 1][Nx - 1] == 0:
                Dist[Ny - 1][Nx - 1] = Dist[y - 1][x - 1] + 1
                Queue.append((Ny, Nx))

    if Dist[N - 1][M - 1] == 0:
        return -1
    else:
        return Dist[N - 1][M - 1] + 1
