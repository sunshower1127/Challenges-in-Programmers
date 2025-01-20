"""배달

다익스트라임.

다익스트라 = 출발노드부터 다른 노드까지의 거리가 최소인것만 힙에 넣고 꺼내면서 탐색하면 됨

"""

from heapq import heappop, heappush


def solution(N, road, K):
    min_dists = [float("inf")] * (N + 1)
    min_dists[1] = 0

    roads = [[float("inf")] * (N + 1) for _ in range(N + 1)]

    for node_a, node_b, dist in road:
        roads[node_a][node_b] = min(roads[node_a][node_b], dist)
        roads[node_b][node_a] = min(roads[node_b][node_a], dist)

    min_heap = [(0, 1)]
    while min_heap:
        dist, node = heappop(min_heap)
        if dist > min_dists[node]:
            continue

        for new_node in range(2, N + 1):
            new_dist = dist + roads[node][new_node]

            if new_dist >= min_dists[new_node]:
                continue

            min_dists[new_node] = new_dist
            heappush(min_heap, (new_dist, new_node))

    return [min_dist <= K for min_dist in min_dists[1:]].count(True)
