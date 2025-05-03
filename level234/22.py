"""[카카오 인턴] 경주로 건설

벽을 피하고
회전을 최소화한
최단거리

근데 회전을 피하느라
더 가는 경우가 존재할 수 있나?
있네요 레전드

어떻게 해야되지
뭐 어떻게 함 그냥 bfs인데 도착했다고 끝이 아닌거임.
모든 경우의 수를 다 탐방해야함
사실상 bfs의 의미가 없어지는거임? dfs로 풀어도 될듯.

400까진 한번 더 넘겨
이게 그러니깐
오케이 온 방향이 다르면 한번은 봐줘!
를 구현하려면

자 -> 머리가 쪼개질거 같으면? 머릿속 메모리가 부족하면 컴퓨터속 메모리를 낭비해라 이거죠
보통 공간복잡도는 안따지거든요 잘

직진인경우와 아닌 경우를 따지기 힘드니깐, 그냥 4방향에서 온거를 다 저장해서 메모리를 4배 낭비하면 된다 이거죠
"""

import sys


def solution(is_rock):
    sys.setrecursionlimit(10**6)
    DY = (1, 0, -1, 0)
    DX = (0, 1, 0, -1)
    dir_iter = list(enumerate(zip(DY, DX)))
    INF = float("inf")
    height = len(is_rock)
    width = len(is_rock[0])
    result = INF

    min_costs = [[[INF] * 4 for _ in range(width)] for _ in range(height)]
    # min_costs[y][x][dir_i]

    def dfs(y, x):
        for dir_i, (dy, dx) in dir_iter:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < height and 0 <= nx < width):
                continue
            if is_rock[ny][nx]:
                continue

            # 회전시
            new_cost = min(min_costs[y][x][i] for i in range(4) if i != dir_i) + 600

            # 직진시
            new_cost = min(new_cost, min_costs[y][x][dir_i] + 100)

            if new_cost < min_costs[ny][nx][dir_i]:
                min_costs[ny][nx][dir_i] = new_cost
                if (ny, nx) == (height - 1, width - 1):
                    nonlocal result
                    result = min(result, new_cost)

                dfs(ny, nx)

    min_costs[0][0] = [0, 0, 0, 0]
    dfs(0, 0)
    return result
