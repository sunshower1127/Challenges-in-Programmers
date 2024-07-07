"""

올바른 괄호

"()()" -> True
")()(" -> False

"""

from collections import deque


def solution(s):
    Stack = deque()
    for c in s:
        if c == "(":
            Stack.append("(")
        else:
            if not Stack:
                return False
            Stack.pop()

    if Stack:
        return False
    else:
        return True
