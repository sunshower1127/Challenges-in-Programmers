"""

피로도

dungeons에는 [최소 필요 피로도, 소모 피로도] 가 담긴 리스트가 있음.

유저의 초기 피로도가 k로 주어짐.
이 때 최대로 돌 수 있는 던전 개수를 구하자.

길이가 변하는 경우의 수 -> dfs, bfs

"""


def solution(k, dungeons):
    N = len(dungeons)
    K = k
    Visited = [False] * N
    Max = 0

    def DFS():
        nonlocal K, Max, Visited
        for i in range(N):
            if Visited[i] or K < dungeons[i][0]:
                continue

        Visited[i] = True
        K -= dungeons[i][1]
        Max = max(Max, Visited.count(True))
        DFS()
        Visited[i] = False
        K += dungeons[i][1]

    DFS()
    return Max
