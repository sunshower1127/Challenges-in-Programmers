"""

JadenCase 문자열 만들기

"for the last week" -> "For The Last Week"
간단

"""


def solution(s):
    s = s.lower()

    str1 = ""
    for i in range(len(s)):
        if i == 0 or s[i - 1] == " ":
            str1 += s[i].upper()
        else:
            str1 += s[i]

    return str1


def gptsolution(s: str):
    return " ".join([word.capitalize() for word in s.split()])
