"""괄호 회전하기
그냥 계속 검증하는 수밖에 없죠 뭐
근데 한 번 구현을 해볼게요.
구현은 안되겠다 매직 메서드들을 잘 모르겟음
"""

from collections import deque

pairs = {"[": "]", "{": "}", "(": ")"}


def validate(container):
    stack = []
    for item in container:
        if item in pairs:
            stack.append(item)
        elif stack and pairs[stack[-1]] == item:
            stack.pop()
        else:
            return False

    return not stack


def solution(s):
    q = deque(s)
    cnt = 0

    for _ in range(len(s)):
        if validate(q):
            cnt += 1
        q.rotate(1)

    return cnt
