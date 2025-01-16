"""

타겟 넘버

각 숫자들 앞에 +혹은 -를 붙여서 target 숫자를 만들 수 있는 경우의 수.

브루트면 2^n. 숫자는 최대 20개. 2^20 = 1000000 -> 가능.

이게 왜 dfs문제지? -> for문을 n개 만들어야하니깐 ㅇㅇ

"""


def solution(numbers, target):
    N = len(numbers)
    Visited = [0] * N
    Cnt = 0

    def DFS(n):
        nonlocal Visited, Cnt
        if n == N - 1:
            if sum(Visited[i] * numbers[i] for i in range(N)) == target:
                Cnt += 1
            return

        Visited[n + 1] = -1
        DFS(n + 1)
        Visited[n + 1] = 1
        DFS(n + 1)
        Visited[n + 1] = 0

    DFS(-1)

    return Cnt
