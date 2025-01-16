"""삼각 달팽이

n = 1000

음.. 대충 넓이하고 비슷하지 않을까요?

n^2 -> 넉넉함

근데 이거 시뮬레이션임.

"""


def solution(n):
    dirs = [(1, 0), (0, 1), (-1, -1)]
    # 배열 기준 아래, 오른쪽, 왼쪽위대각선

    dirs_i = 0
    mat = [[0] * n for _ in range(n)]
    y, x = 0, 0
    num = 1
    while True:
        mat[y][x] = num
        num += 1

        for i in range(3):
            # 0, 1, 2
            dirs_i += i
            dirs_i %= 3

            dy, dx = dirs[dirs_i]
            ny, nx = y + dy, x + dx

            if 0 <= ny < n and 0 <= nx < n and mat[ny][nx] == 0:
                y, x = ny, nx
                break

        else:  # no break
            break

    result = []

    for y in range(n):
        for x in range(n):
            if mat[y][x] == 0:
                break

            result.append(mat[y][x])

    return result
