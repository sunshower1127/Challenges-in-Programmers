"""

배달

1번마을에서 거리가 K 이하인 마을의 개수 구하기

총 거리 구하는거니깐 dfs가 맞는거 같죠

아니 다익스트라도 디테일이 좀 중요하네

1. 시작 노드로 다시 가면 안됨

2. 아직 모름 근데 뭔가 또 디테일이 있나봄 -> 최대거리를 계속 더하면 수가 커짐.

최대값 계산하기 귀찮고, 또 로깅할때 float("inf")는 숫자가 아니라 inf 라고 나오니깐 자주 쓰도록 하자.

if가 중첩일때 and로 저렇게 푸는것도 좋긴한데
저러면 로깅이 불편하지 않나
그냥 죄다 not 처리해버리는게 나을수도
"""

from heapq import heappop, heappush


def solution(N, road, K):
    road += [[b, a, dist] for a, b, dist in road]

    dists = [float("inf")] * (N + 1)
    min_heap = [(0, 1)]

    while min_heap:
        dist, node = heappop(min_heap)

        for from_node, new_node, new_dist in road:
            if not (from_node == node and new_node != 1):
                print("1번 조건 실패")
                continue
            if (total_dist := dist + new_dist) >= dists[new_node]:
                print("2번 조건 실패")
                continue

            dists[new_node] = total_dist
            heappush(min_heap, (total_dist, new_node))
        ##

    return len([0 for dist in dists if dist <= K]) + 1
    ##


def dfs_solution(N, road, K):
    visited = set()
    result = set()
    dist_sum = 0

    def dfs(v):
        nonlocal dist_sum
        for a, b, dist in road:
            if a == v and b not in visited and dist_sum + dist <= K:
                visited.add(b)
                result.add(b)
                dist_sum += dist
                dfs(b)
                visited.remove(b)
                dist_sum -= dist
        ##

    visited.add(1)
    result.add(1)
    dfs(1)

    return len(result)
