"""

배달

1번마을에서 거리가 K 이하인 마을의 개수 구하기

총 거리 구하는거니깐 dfs가 맞는거 같죠

"""


def solution(N, road, K):
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
