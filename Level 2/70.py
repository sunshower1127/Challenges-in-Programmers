"""
행렬 테두리 회전하기

굉장히 헷갈렸음. 구현자체도 회전은 처음 구현해보는거였고
행렬에서 계속 y하고 x가 헷갈려서 (+- 방향이나 행,열)
심지어 문제에서도 y하고 x를 거꾸로줬음 좌표하고 비교해서

일단 남들 푼거 보고, ai한테도 물어보고 그럴게요 처음푸는 문제 유형이라서

tip : 디버깅할때 가장 작은 케이스만 if문으로 처음에 걸러내면 편하다
tip2 : 굳이 dir 가지고 탐색할게 아니라 그냥 for문 상하좌우 4개 쓰는것도 좋았을듯.
tip3 : d하고 d_i 쓸바엔 iter하고 next 쓰는게 나았을듯.
"""


def solution(rows, columns, queries):
    mat = [[0] * columns for _ in range(rows)]
    result = []

    for y in range(rows):
        for x in range(columns):
            mat[y][x] = y * columns + x + 1
        ##

    for y1, x1, y2, x2 in queries:
        y, x = y1, x1
        v = mat[y][x - 1]
        d = [(), (0, 1), (1, 0), (0, -1), (-1, 0)]
        d_i = 0
        min_v = v
        while True:
            temp = mat[y - 1][x - 1]
            mat[y - 1][x - 1] = v
            v = temp
            if v < min_v:
                min_v = v

            if y == y1 + 1 and x == x1:
                break

            if y in (y1, y2) and x in (x1, x2):
                d_i += 1

            y += d[d_i][0]
            x += d[d_i][1]
            ##

        mat[y1 - 1][x1 - 1] = v
        result.append(min_v)
        ##

    return result


def solution2(rows, columns, queries):
    mat = [[0] * columns for _ in range(rows)]
    result = []

    for y in range(rows):
        for x in range(columns):
            mat[y][x] = y * columns + x + 1
        ##

    for y1, x1, y2, x2 in queries:
        y, x = y1, x1
        v = mat[y][x - 1]
        dirs = iter([(0, 1), (1, 0), (0, -1), (-1, 0)])
        min_v = v
        while True:
            temp = mat[y - 1][x - 1]
            mat[y - 1][x - 1] = v
            v = temp
            min_v = min(v, min_v)

            if y == y1 + 1 and x == x1:
                break

            if y in (y1, y2) and x in (x1, x2):
                dir = next(dirs)

            y += dir[0]
            x += dir[1]
            ##

        mat[y1 - 1][x1 - 1] = v
        result.append(min_v)
        ##

    return result


def ai_solution(rows, columns, queries):
    # 초기 행렬 생성
    matrix = [
        [col + row * columns + 1 for col in range(columns)] for row in range(rows)
    ]
    result = []

    # 방향 배열: 오른쪽, 아래, 왼쪽, 위
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for y1, x1, y2, x2 in queries:
        y1, x1, y2, x2 = y1 - 1, x1 - 1, y2 - 1, x2 - 1  # 인덱스 조정
        prev_value = matrix[y1][x1]
        min_value = prev_value
        y, x = y1, x1

        for dy, dx in directions:
            while True:
                ny, nx = y + dy, x + dx
                if ny < y1 or ny > y2 or nx < x1 or nx > x2:
                    break
                matrix[y][x] = matrix[ny][nx]
                min_value = min(min_value, matrix[ny][nx])
                y, x = ny, nx

        matrix[y1][x1 + 1] = prev_value  # 마지막 값 복원
        result.append(min_value)

    return result
