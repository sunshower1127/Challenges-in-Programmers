"""JadenCase 문자열 만들기

python의 lower, upper는 그냥 문자열 안에 뭐가 들어있든 싹다 작동시키고
capitalize는 첫 단어만 작동함.

"""

import re


def solution(s):
    s = re.sub(r"\w+", lambda m: m.group(0).capitalize(), s)
    return s


""" 이게 정석이긴하고 """
def solution2(s):
    s = s.lower()

    result = []
    for word in s.split(" "):
        if word:
            result.append(word[0].upper() + word[1:])
        else:
            result.append("") # 빈 문자열인 경우 어떻게 처리할지 결정 (빈 문자열 유지, 무시 등)

    return " ".join(result)