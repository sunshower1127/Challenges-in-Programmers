"""

괄호 회전하기

괄호들이 주어지는데, 이걸 왼쪽으로 x만큼 이동시키면 괄호가 정상이 됨. x를 구하자

tip : 왼쪽으로 회전 -> 이미지를 떠올려보면 왼쪽이 없어지고 오른쪽이 생김. deque를 이용하자.
tip2 : 사실 얘도 원형문제라서 *2를 하는게 쉽긴 하다.
"""

from collections import deque


def solution(s):
    opposite = {"[": "]", "{": "}", "(": ")"}
    N = len(s)
    s = s * 2
    cnt = 0
    for i in range(N):
        stack = deque()
        break1 = False
        for j in range(N):
            if s[i + j] in opposite:
                stack.append(s[i + j])
            else:
                if stack and opposite[stack.pop()] == s[i + j]:
                    continue
                else:
                    break1 = True
                    break
        if not stack and not break1:
            cnt += 1

    return cnt


# deque.rotate(n) 를 사용해도 된다. n이 양수면 오른쪽 이동, n이 음수면 왼쪽이동.
