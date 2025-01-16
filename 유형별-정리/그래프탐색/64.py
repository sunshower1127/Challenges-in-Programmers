"""전력망을 둘로 나누기

100 * 100

그냥 브루트네요
거기다 이제 트리 탐색을 더한
검색이 용이해야해서 set에다가 집어넣읍시다.
암튼 그래프 탐색 맞음. 굳.

defaultdict쓰면 엄청 편하네요 굳.

"""

from collections import defaultdict


def solution(n, wires):
    min_gap = float("inf")

    new_wires = defaultdict(set)
    for node1, node2 in wires:
        new_wires[node1].add(node2)
        new_wires[node2].add(node1)

    for cut in wires:
        visited = [False] * (n + 1)

        stack = [cut[0]]
        visited[cut[0]] = True
        visited[cut[1]] = True  # 반대편이라서 나중에 1 뺴줘야함

        while stack:
            node = stack.pop()

            for new_node in new_wires[node]:
                if visited[new_node]:
                    continue

                visited[new_node] = True
                stack.append(new_node)

        size = visited.count(True) - 1  # 반대편 노드 한개 빼주기
        oppo_size = n - size

        min_gap = min(min_gap, abs(size - oppo_size))

    return min_gap
