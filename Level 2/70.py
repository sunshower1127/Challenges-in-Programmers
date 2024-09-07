"""
행렬 테두리 회전하기

일단 초안 만들어봄.

"""


def solution(rows, columns, queries):
    map = [[0] * columns for _ in range(rows)]
    result = []

    for y in range(rows):
        for x in range(columns):
            map[y][x] = y * columns + x + 1
        ##

    for x1, y1, x2, y2 in queries:
        y, x = y1, x1
        v = map[y - 2][x - 1]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        d_i = 0
        min_v = v
        while True:
            temp = map[y - 1][x - 1]
            map[y - 1][x - 1] = v
            v = temp
            if v < min_v:
                min_v = v

            if y == y1 - 1 and x == x1:
                break

            if y in (y1, y2) and x in (x1, x2):
                d_i += 1

            y += d[d_i][0]
            x += d[d_i][1]
            ##

        map[y1 - 1][x1 - 1] = v
        result.append(min_v)
        ##

    return result
