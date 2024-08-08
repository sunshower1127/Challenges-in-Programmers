"""
3진수인지 알았는데 아니네요
2진수?
그냥 노가다하는게 베스트인듯.

사전순 그 문제랑 비슷하네
어떻게 풀었더라
dfs?

규칙 찾기 귀찮아서 그냥 bfs로 풀려고 했는데
왜냐면 n이 500,000,000이라서 O(n) 통과...
안되네 5억이잖아. 1억안에 풀어야하는데
왜 헷갈렸는지 모르겠는데 암튼
패턴 찾기임. 근데 귀찮아서 안함. 이런류 문제는 솔직히 영양가 없다고 생각해서.
"""

from collections import deque


def solution(n):
    q = deque()
    q.append("")
    cnt = 0
    while q:
        num = q.popleft()

        for i in ("1", "2", "4"):
            new_num = num + i
            cnt += 1
            if cnt == n:
                return new_num
            q.append(new_num)


def solution2(n):
    answer = []

    while n:
        tmp = n % 3
        if tmp == 0:
            tmp = 4
            n -= 1
        answer.append(str(tmp))
        n //= 3

    answer.reverse()
    return "".join(answer)
