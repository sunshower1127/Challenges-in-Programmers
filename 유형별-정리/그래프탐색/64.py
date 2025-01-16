"""

전력망을 둘로 나누기

전선 하나 끊었을때, 송전탑개수의 차의 최소를 구하시오

n=100이고, 대충 e,v가 100개씩임.

그냥 하나 끊어서, 양쪽 탐색 -> 100 100 이니깐 뭐 100000정도? -> 가능

1. 양쪽 탐색할 필요 없음 -> 한쪽만 구하고, 어차피 다 연결되어있으니깐 n - cnt 하면 됨.
2. visited를 set으로 바꾸면, in연산이 O(1)이라서 더 빠름.

"""


def solution(n, wires):
    answer = 101
    banned = 0
    visited = []

    def dfs(v):
        visited.append(v)
        for a, b in wires:
            if a == v and b != banned and b not in visited:
                dfs(b)
            if b == v and a != banned and a not in visited:
                dfs(a)

    for a, b in wires:
        visited = []
        banned = b
        dfs(a)
        cnta = len(visited)

        visited = []
        banned = a
        dfs(b)
        cntb = len(visited)

        answer = min(answer, abs(cnta - cntb))

    return answer if answer != 101 else -1


def solution2(n, wires):
    answer = n

    def dfs(v, banned, visited):
        visited.add(v)
        for a, b in wires:
            if a == v and b != banned and b not in visited:
                dfs(b, banned, visited)
            if b == v and a != banned and a not in visited:
                dfs(a, banned, visited)

    for a, b in wires:
        visited = set()
        dfs(a, b, visited)
        cnta = len(visited)
        cntb = n - cnta
        answer = min(answer, abs(cnta - cntb))

    return answer
