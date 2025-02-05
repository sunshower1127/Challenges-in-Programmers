"""가장 먼 노드

bfs 쓰면 될거 같음

? 어디서 이렇게 시간 차이가 많이 나는거임?

for next_node in [*unvisited]:
    if next_node in edges[node]:

하고

for next_node in edges[node]:
    if next_node in unvisited:

하고

시간 차이가 왜이렇게 많이 나죠?
node가 20000개고
음... 그럴만한가

확실히 for문 돌아가는 숫자를 확 줄이는게 중요함
일단 늘리고 조건문으로 없앤다? X
무조건 줄여라 O

그리고 set을 반복문에다 넣으면
generator라서
도중에 set에 변경이 일어나면
에러남 조심
그래서 list로 바꿔서 넣던가 아니면 체크만 하던가
"""

from collections import defaultdict, deque


def solution(n, edge):
    mem = [0, 1]

    edges = defaultdict(set)

    for a, b in edge:
        a -= 1
        b -= 1
        edges[a].add(b)
        edges[b].add(a)

    q = deque()
    unvisited = {*range(n)}

    q.append((0, 0))
    unvisited.remove(0)

    while q:
        node, dist = q.popleft()

        new_dist = dist + 1
        for next_node in edges[node]:
            if next_node in unvisited:
                q.append((next_node, new_dist))
                unvisited.remove(next_node)

                if new_dist > mem[0]:
                    mem[0] = new_dist
                    mem[1] = 0
                mem[1] += 1

    return mem[1]
