"""

올바른 괄호

"()()" -> True
")()(" -> False

"""

from collections import deque


def solution(s):
    stack1 = deque()
    for c in s:
        if c == "(":
            stack1.append("(")
        else:
            if not stack1:
                return False
            stack1.pop()

    if stack1:
        return False
    else:
        return True
