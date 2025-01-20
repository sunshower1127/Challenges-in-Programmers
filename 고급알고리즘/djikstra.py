import heapq


def dijkstra(start, graph):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if distances[current_node] < current_dist:
            continue
        for adjacent, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    return distances


"""그리디는 맞음.
그리디의 주체는 이제 1번 노드로부터 다른 노드까지의 거리
최소힙에다가 넣고, 제일 작은것부터 뽑는거임.

출발 노드로부터 제일 가까운 노드부터 계속 뽑아나가면 최단거리가 나오게 된다
라네요.
그리디는 너무 파고들면 머리아픔 여기까지만 알자.
"""
