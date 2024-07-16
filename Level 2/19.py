"""

괄호 회전하기

괄호들이 주어지는데, 이걸 왼쪽으로 x만큼 이동시키면 괄호가 정상이 됨. x를 구하자

tip : 왼쪽으로 회전 -> 이미지를 떠올려보면 왼쪽이 없어지고 오른쪽이 생김.
deque를 이용하자.
tip2 : 사실 얘도 원형문제라서 *2를 하는게 쉽긴 하다.
"""

from collections import deque


def solution(s):
    Oppo = {"[": "]", "{": "}", "(": ")"}
    N = len(s)
    s = s * 2
    Cnt = 0

    for i in range(N):
        Stack = deque()
        Break = False
        for j in range(N):
            if s[i + j] in Oppo:
                Stack.append(s[i + j])
            else:
                if Stack and Oppo[Stack.pop()] == s[i + j]:
                    continue

                Break = True
                break
        if not Stack and not Break:
            Cnt += 1

    return Cnt


# deque.rotate(n) 를 사용해도 된다. n이 양수면 오른쪽 이동, n이 음수면 왼쪽이동.
