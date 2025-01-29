"""단어 변환

한번에 한개씩만.

타서 갔을때

최소거리.

bfs네요


"""

from collections import deque


def solution(begin, target, words):
    N = len(begin)
    q = deque()
    q.append((begin, 0))

    while q:
        word, visited = q.popleft()

        for i, next_word in enumerate(words):
            if 1 << i & visited:
                continue
            if [word[i] == next_word[i] for i in range(N)].count(False) != 1:
                continue

            if next_word == target:
                return bin(visited).count("1") + 1

            q.append((next_word, 1 << i | visited))

    return 0
