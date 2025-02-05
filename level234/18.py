"""여행경로

일단 전체 경로를 출력해야하고
알파벳 순으로 진행해야함.

딱 하나만 찝는건 역시 dfs다.
저 if result: return 이 사기임

visited를 그냥 edge에다가 박아버리는 것도 dfs라 가능한거고
"""

from collections import defaultdict


def solution(tickets):
    edges = defaultdict(list)

    for start, end in tickets:
        edges[start].append([end, False])  # next_node, visited

    for key in edges:
        edges[key].sort()

    path = ["ICN"]
    result = []

    def dfs():
        if len(path) == len(tickets) + 1:
            nonlocal result
            result = path[:]

        if result:
            return

        node = path[-1]
        for next_data in edges[node]:
            next_node, visited = next_data
            if visited:
                continue

            next_data[1] = True
            path.append(next_node)
            dfs()
            next_data[1] = False
            path.pop()

    dfs()
    return result
