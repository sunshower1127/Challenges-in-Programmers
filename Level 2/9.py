"""

짝지어 제거하기

붙어있는 2개의 같은 문자를 터뜨리며 제거
baabaa -> bbaa -> aa -> 빔

다 제거 가능 -> 1반환, 아니면 0반환

tip : 문자열 -> 1차원이므로 스택 넣어서 풀면 됨.
"""

from collections import deque


def solution(s):
    stack1 = deque()
    for c in s:
        if stack1 and stack1[-1] == c:
            stack1.pop()
        else:
            stack1.append(c)

    if stack1:
        return 0
    else:
        return 1
