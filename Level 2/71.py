"""
행렬 테두리 회전하기

굉장히 헷갈렸음. 구현자체도 회전은 처음 구현해보는거였고
행렬에서 계속 y하고 x가 헷갈려서 (+- 방향이나 행,열)
심지어 문제에서도 y하고 x를 거꾸로줬음 좌표하고 비교해서

일단 남들 푼거 보고, ai한테도 물어보고 그럴게요 처음푸는 문제 유형이라서

tip : 디버깅할때 가장 작은 케이스만 if문으로 처음에 걸러내면 편하다

"""


def solution(rows, columns, queries):
    map = [[0] * columns for _ in range(rows)]
    result = []

    for y in range(rows):
        for x in range(columns):
            map[y][x] = y * columns + x + 1
        ##

    for y1, x1, y2, x2 in queries:
        y, x = y1, x1
        v = map[y][x - 1]
        d = [(), (0, 1), (1, 0), (0, -1), (-1, 0)]
        d_i = 0
        min_v = v
        while True:
            temp = map[y - 1][x - 1]
            map[y - 1][x - 1] = v
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

        map[y1 - 1][x1 - 1] = v
        result.append(min_v)
        ##

    return result
