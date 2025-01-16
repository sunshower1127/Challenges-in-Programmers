"""석유 시추
덩어리의 넓이 + 차지하는 x좌표
이거 두개를 가지고 있으면 계산이 쉽겠죠
dfs든 bfs든 할때
"""

DX = [0, 1, 0, -1]
DY = [1, 0, -1, 0]


def search(sy, sx, Y, X, visited):
    stack = [(sy, sx)]

    amount = 1
    visited[sy][sx] = True
    min_x = max_x = sx
    while stack:
        y, x = stack.pop()

        for dy, dx in zip(DY, DX):
            ny, nx = y + dy, x + dx
            if not (0 <= ny < Y):
                continue
            if not (0 <= nx < X):
                continue
            if visited[ny][nx]:
                continue

            amount += 1
            visited[ny][nx] = True
            min_x = min(min_x, nx)
            max_x = max(max_x, nx)

            stack.append((ny, nx))

    return min_x, max_x, amount


def solution(land):
    Y = len(land)
    X = len(land[0])
    result = [0] * X
    visited = [[land[y][x] == 0 for x in range(X)] for y in range(Y)]
    for y in range(Y):
        for x in range(X):
            if visited[y][x]:
                continue
            x1, x2, amount = search(y, x, Y, X, visited)
            result[x1 : x2 + 1] = [n + amount for n in result[x1 : x2 + 1]]

    return max(result)
