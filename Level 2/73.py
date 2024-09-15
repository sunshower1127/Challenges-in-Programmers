"""
다시 지나갈 수 있다는게 핵심이네요
dfs가 아니라서 경로를 모름
그냥 레버 유무만 넣읍시다.
거리 유무도 넣어야겠는데?

최적화가 필요함.

다시 돌아온다 -> 이거에 조건을 좀 걸어야할듯.
맵에다가. Lever유무를 적는거죠. 그래서
두개를 만들어. lever 전이랑 후.

bfs에 대해서 너무 대비가 안되어있었다..
dirs도 그렇고
dists 만들때 X, Y 순서인것도 헷갈렸고
여러모로... 수난이네요

"""

from collections import deque


def solution(maps):
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    Y, X = len(maps), len(maps[0])

    def find_value(c):
        for y in range(Y):
            for x in range(X):
                if maps[y][x] == c:
                    return y, x
        ##

    def bfs(start, end):
        sy, sx = find_value(start)

        dists = [[0] * X for _ in range(Y)]
        dists[sy][sx] = 1

        q = deque()
        q.append((sy, sx))

        while q:
            y, x = q.popleft()
            for dy, dx in dirs:
                ny, nx = y + dy, x + dx

                if not (0 <= ny < Y and 0 <= nx < X):
                    continue
                if dists[ny][nx] > 0:
                    continue
                v = maps[ny][nx]
                if v == "X":
                    continue
                if v == end:
                    return dists[y][x]

                dists[ny][nx] = dists[y][x] + 1
                q.append((ny, nx))

            ##
        return -1
        ##

    if (dist_to_lever := bfs("S", "L")) == -1 or (dist_to_end := bfs("L", "E")) == -1:
        return -1

    return dist_to_lever + dist_to_end
