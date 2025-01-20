# 유명한 MST 알고리즘: Prim, Kruskal
import heapq


def prim(graph, start):
    """visited랑 unvisited를 연결하는 가장 짧은 edge들만 찾아주면 됨."""
    visited = set()
    mst = []
    edges = []
    visited.add(start)
    for neighbor, cost in graph[start]:
        heapq.heappush(edges, (cost, start, neighbor))
    while edges and len(visited) < len(graph):
        cost, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, cost))
            for nxt, nxt_cost in graph[v]:
                if nxt not in visited:
                    heapq.heappush(edges, (nxt_cost, v, nxt))
    return mst


def kruskal(edges, n):
    """edge들을 짧은 순으로 탐색하고
    서로 다른 집합의 노드들을 연결해주면 됨.
    이게 구현이 좀 어렵네요 근데 트리 형태로 이어주는거 같은데
    rank가 이제 내 자식 노드들 개수를 의미하고
    parent가 내 노드의 부모 노드 번호.
    해서 큰 트리가 작은 트리를 아래다 다는 식으로 관리 ㅇㅇ
    """
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        rootA = find(a)
        rootB = find(b)
        if rootA != rootB:
            if rank[rootA] < rank[rootB]:
                parent[rootA] = rootB
            elif rank[rootA] > rank[rootB]:
                parent[rootB] = rootA
            else:
                parent[rootB] = rootA
                rank[rootA] += 1
            return True
        return False

    mst = []
    edges.sort(key=lambda x: x[2])
    for u, v, cost in edges:
        if union(u, v):
            mst.append((u, v, cost))
    return mst
