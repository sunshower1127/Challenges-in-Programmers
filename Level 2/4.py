"""

JadenCase 문자열 만들기

"for the last week" -> "For The Last Week"
간단

"""


def solution(s):
    s = s.lower()

    Str = ""
    for i in range(len(s)):
        if i == 0 or s[i - 1] == " ":
            Str += s[i].upper()
        else:
            Str += s[i]

    return Str


def gptsolution(s: str):
    return " ".join([word.capitalize() for word in s.split()])
