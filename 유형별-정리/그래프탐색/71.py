"""무인도 여행

면적구하기는 dfs, bfs 뭘 써도 똑같음.

"""


def get_food_amount(sy, sx, height, width, maps, visited):
    stack = [(sy, sx)]
    DY = [1, 0, -1, 0]
    DX = [0, 1, 0, -1]
    food_amount = int(maps[sy][sx])
    visited[sy][sx] = True

    while stack:
        y, x = stack.pop()

        for dy, dx in zip(DY, DX):
            ny, nx = y + dy, x + dx

            if not (0 <= ny < height and 0 <= nx < width):
                continue
            if maps[ny][nx] == "X":
                continue
            if visited[ny][nx]:
                continue

            stack.append((ny, nx))
            visited[ny][nx] = True
            food_amount += int(maps[ny][nx])

    return food_amount


def solution(maps):
    height = len(maps)
    width = len(maps[0])
    visited = [[False] * width for _ in range(height)]
    result = []

    for y in range(height):
        for x in range(width):
            if maps[y][x] != "X" and not visited[y][x]:
                result.append(get_food_amount(y, x, height, width, maps, visited))

    return sorted(result) if result else [-1]
