"""부대 복귀

여기저기 퍼져있는 애들을 한 곳으로 복귀시켜야함.

그냥 다익스트라인데요

시작하는 곳에서부터 노드의 거리를 계속해서 갱신해나가면 됨.
"""

from collections import defaultdict
from heapq import heappop, heappush


def solution(n, roads, sources, destination):
    min_dists = [float("inf")] * (n + 1)

    road_dict = defaultdict(set)

    for a, b in roads:
        road_dict[a].add(b)
        road_dict[b].add(a)

    min_heap = [(0, destination)]
    min_dists[destination] = 0

    while min_heap:
        dist, node = heappop(min_heap)

        if dist > min_dists[node]:
            continue

        for next_node in road_dict[node]:
            if dist + 1 < min_dists[next_node]:
                min_dists[next_node] = dist + 1
                heappush(min_heap, (dist + 1, next_node))

    return [
        min_dists[node] if min_dists[node] != float("inf") else -1 for node in sources
    ]
