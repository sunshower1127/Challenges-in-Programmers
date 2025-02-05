"""짝지어 제거하기

이건 문자열에다가 넣어야돼 뭐 어떻게 해야돼
일단 정규식 쓰면 시간 초과됨.

계속해서 줄여나가는거라서 ㅇㅇ
이런 경우는 스택을 써서 최적화를 해줘야한다.
"""

import re


def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if stack:
        return 0
    else:
        return 1


def resolution(s):
    pattern = re.compile(r"([a-z])\1")

    while pattern.search(s):
        s = pattern.sub("", s)

    return 0 if s else 1
