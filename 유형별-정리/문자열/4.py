"""JadenCase 문자열 만들기

python의 lower, upper는 그냥 문자열 안에 뭐가 들어있든 싹다 작동시키고
capitalize는 첫 단어만 작동함.

"""

import re


def solution(s):
    s = re.sub(r"\w+", lambda m: m.group(0).capitalize(), s)
    return s
