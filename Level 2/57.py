"""

삼각 달팽이

피라미드에서 가장자리를 돌아가면서 중심으로 점점 이동.
숫자를 1차원 배열로 만들어서 리턴.

예)
N = 4
1
2 9
3 10 8
4 5 6 7

[1, 2, 9, 3, 10, 8, 4, 5, 6, 7]

tip1. 재귀 함수로 풀려면 sys.setrecursionlimit(10**6)을 해주자. 귀찮구만..
tip2. 방향은 3개가 순서대로 계속 반복됨. Dir[i:=(i+1)%3] 이런식으로 간단한 체인은 쉽게 구현할 수 있다.

어찌보면 시뮬레이션이라 그냥 그대로 구현해봤다.

dfs는 함수고, bfs는 큐를 사용한 for문이다. 라는 차이가 의미있는건 -> 다양한 경우의수가 나타날때,
어떤걸 우선으로 탐색할지에 대한 이야기다.
dfs는 깊이 우선 탐색 -> 그냥 쭉 들어가서 답부터 찾고 본다.
bfs는 너비 우선 탐색 -> 한 level의 모든 경우의수를 따져가며 탐색한다.

이 문제는 여러 경우의 수가 나타나는게 아니기 때문에, 함수로 풀던 for로 풀던 상관없음.

"""

import sys


def solution(N):
    sys.setrecursionlimit(10**6)
    Map = [[0] * (n + 1) for n in range(N)]
    Dir = [(1, 0), (0, 1), (-1, -1)]
    cnt = 1

    def dfs(y, x, dir):
        nonlocal cnt
        Map[y][x] = cnt

        cnt += 1

        ny, nx = y + Dir[dir][0], x + Dir[dir][1]
        if 0 <= ny < N and 0 <= nx <= ny and Map[ny][nx] == 0:
            dfs(ny, nx, dir)
            return

        for ndir in range(3):
            if ndir == dir:
                continue
            ny, nx = y + Dir[ndir][0], x + Dir[ndir][1]
            if 0 <= ny < N and 0 <= nx <= ny and Map[ny][nx] == 0:
                dfs(ny, nx, ndir)
                return

    dfs(0, 0, 0)
    result = []
    for line in Map:
        result.extend(line)

    return result


# AI 수정 코드


def solution2(N):
    Map = [[0] * (n + 1) for n in range(N)]
    Dir = [(1, 0), (0, 1), (-1, -1)]
    cnt = 1
    y, x, dir = 0, 0, 0

    while cnt <= N * (N + 1) // 2:
        Map[y][x] = cnt
        cnt += 1

        ny, nx = y + Dir[dir][0], x + Dir[dir][1]
        if not (0 <= ny < N and 0 <= nx <= ny and Map[ny][nx] == 0):
            dir = (dir + 1) % 3
            ny, nx = y + Dir[dir][0], x + Dir[dir][1]

        y, x = ny, nx

    result = []
    for line in Map:
        result.extend(line)

    return result
