"""

무인도 여행

전형적인 이제 dfs문제?
bfs든 dfs든 상관 없을듯.

X는 바다, 숫자는 땅
각 땅의 넓이를 구하고, 오름차순으로 정렬해서 리턴

tip 1: setrecursionlimit 진짜 함수명 당황스럽긴하다
tip 2: str를 수정할게 아니라면 굳이 list로 안바꿔도 됨
tip 3: 좌표문제는 왠만하면 bfs로 풀자.
"""

from sys import setrecursionlimit


def solution(maps):
    setrecursionlimit(10**8)
    Y = len(maps)
    X = len(maps[0])
    visited = [[False] * X for _ in range(Y)]
    maps = list(map(list, maps))
    result = []
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(y, x):
        nonlocal dfs_sum
        dfs_sum += int(maps[y][x])
        visited[y][x] = True

        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < Y and 0 <= nx < X):
                continue
            if visited[ny][nx]:
                continue
            if maps[ny][nx] == "X":
                continue

            dfs(ny, nx)

    for y in range(Y):
        for x in range(X):
            if maps[y][x] != "X" and not visited[y][x]:
                dfs_sum = 0
                dfs(y, x)
                result.append(dfs_sum)
        ##

    result.sort()
    return result if result else [-1]
