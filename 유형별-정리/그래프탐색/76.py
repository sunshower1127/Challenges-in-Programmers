"""리코쳇 로봇

bfs로 그냥 체크하면서 이동하면 될거같긴함.

tip: bfs에서 초기지점에서 값을 1로하고, 마지막엔 -1을 해줘야한다 -> 안그러면 특정 케이스에서 실패뜸.
왜인지는 자세히는 모르겠음. 어차피 시작지점에 다시 한 번 가도, 최소거리기때문에 무시되잖아

시작지점하고 끝지점이 겹쳐있는것밖에 예외케이스가 생각안나는데, 이건 말이 안되잖아
사실 잘 모르겟음.

"""

from collections import deque

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
board = []


def forward(y, x, dy, dx):
    ny = y + dy
    nx = x + dx
    if not (0 <= ny < Y and 0 <= nx < X):
        return (y, x)
    if board[ny][nx] == "D":
        return (y, x)

    return forward(ny, nx, dy, dx)


def solution(_board):
    global Y, X, board, gy, gx
    Y = len(_board)
    X = len(_board[0])

    board: list[list[int | str]] = [[0] * X for _ in range(Y)]

    for y in range(Y):
        for x in range(X):
            if _board[y][x] == "R":
                ry, rx = y, x
            elif _board[y][x] == "G":
                gy, gx = y, x
            elif _board[y][x] == "D":
                board[y][x] = "D"

    q = deque()
    q.append((ry, rx))
    board[ry][rx] = 1

    while q:
        y, x = q.popleft()

        for dy, dx in dirs:
            ny, nx = forward(y, x, dy, dx)
            if board[ny][nx] == 0 or board[ny][nx] > board[y][x] + 1:
                board[ny][nx] = board[y][x] + 1
                q.append((ny, nx))

            if (ny, nx) == (gy, gx):
                return board[ny][nx] - 1

    return -1
