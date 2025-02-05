"""괄호 변환

균형잡힘 -> (와 )가 개수가 같음
올바름 -> 균형잡힘 + 짝도맞음

균형잡힘 -> 올바름 으로 변환

w = u + v (u는 더이상 분리 x)

u를 일단 분리하는 로직이 필요하겠네요

tip 1: 괄호 종류가 하나면 사실 stack 쓸 필요 없이 cnt 만으로 구현 가능함.
tip 2: 균형잡힌거 판단하는 것도 함수로 모듈화 했으면 좋았을듯
"""


def 올바른(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append("(")
        else:
            if stack:
                stack.pop()
            else:
                return False
            ##

    return not stack
    ##


def reverse(s):
    return "".join(")" if c == "(" else "(" for c in s)


def split(w):
    if not w:
        return ""
    left_cnt = 0
    right_cnt = 0
    for i in range(len(w)):
        if w[i] == "(":
            left_cnt += 1
        else:
            right_cnt += 1

        if left_cnt == right_cnt:
            u = w[: i + 1]
            v = w[i + 1 :]
            if 올바른(u):
                return u + split(v)
            else:
                temp = f"({split(v)})"
                temp += reverse(u[1:-1])
                return temp

    return ""
    ##


def solution(p):
    return split(p)
