"""리코쳇 로봇

bfs로 그냥 체크하면서 이동하면 될거같긴함.


"""

from collections import deque


def forward(y, x, dy, dx, board, height, width):
    cnt = 0
    while True:
        y += dy
        x += dx

        if not (0 <= y < height and 0 <= x < width):
            return cnt
        if board[y][x] == "D":
            return cnt

        cnt += 1


def solution(board):
    height = len(board)
    width = len(board[0])

    for y in range(height):
        for x in range(width):
            if board[y][x] == "R":
                sy, sx = y, x
                break

    q = deque()
    visited = [[False] * width for _ in range(height)]

    q.append((sy, sx, 0))
    visited[sy][sx] = True

    DY = [1, 0, -1, 0]
    DX = [0, 1, 0, -1]
    while q:
        y, x, dist = q.popleft()

        for dy, dx in zip(DY, DX):
            n = forward(y, x, dy, dx, board, height, width)
            if n == 0:
                continue

            ny = y + n * dy
            nx = x + n * dx

            if visited[ny][nx]:
                continue
            if board[ny][nx] == "G":
                return dist + 1
            q.append((ny, nx, dist + 1))
            visited[ny][nx] = True

    return -1
