"""올바른 괄호

괄호가 한종류면 그냥 cnt만 써도 된다.
"""


def solution(s):
    cnt = 0

    for c in s:
        if c == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt == -1:
                return False

    return cnt == 0
