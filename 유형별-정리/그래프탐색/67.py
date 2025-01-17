"""배달

다익스트라라고 하네요

다익스트라 -> 특정 노드에부터 다른 노드까지의 모든 거리를 구할 수 있음.

도로가 2000개. 마을이 50개

굳이 최소힙으로 최적화 안해도 되긴함.

다익스트라가 내가 이해하기로는
방문한 노드 집합은 각각 자신의 최소거리를 알고 있고
방문하지 않은 노드 집합과 방문한 노드 집합간의 거리중에서 최소만 선택해나가면
된다는거 같은데
방문한 노드 집합과 방문안한 노드 집합 사이의 엣지들은 재사용 가능하니깐 최소힙에다 넣으면 된다.

TODO: 다익스트라 나중에 한 번 더 정비해서 보기. 일단 포기
"""

from heapq import heappop, heappush


def solution(N, roads, K):
    road_dists = [[float("inf")] * (N + 1) for _ in range(N + 1)]

    for a, b, dist in roads:
        road_dists[a][b] = min(road_dists[a][b], dist)
        road_dists[b][a] = min(road_dists[b][a], dist)

    visited = set()
    unvisited = set(range(1, N + 1))

    min_heap = [(0, 0, 1)]
    min_dists = [float("inf")] * (N + 1)
    min_dists[0] = 0

    while min_heap:
        dist, node_start, node_end = heappop(min_heap)

        if node_end not in unvisited:
            continue

        new_dist = min_dists[node_start] + dist

        if new_dist >= min_dists[node_end]:
            continue

        min_dists[node_end] = new_dist

        visited.add(node_end)
        unvisited.remove(node_end)

        for new_node in unvisited:
            road_dist = road_dists[new_node][node_end]
            if road_dist == float("inf"):
                continue

            heappush(min_heap, (road_dist, node_end, new_node))

    return [min_dist <= K for min_dist in min_dists].count(True) - 1
