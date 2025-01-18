"""[3차] 파일명 정렬"""

import re


def get_key(v):
    match = re.match(r"(.+?)([0-9]+)", v)
    return (match.group(1).lower(), int(match.group(2)))


def solution(files):
    files.sort(key=get_key)
    return files


"""아래는 한줄풀이긴한데 그냥 보셈 js였으면 이게 정석이였음

import re;solution=lambda f:sorted(f,key=lambda v:[m:=re.match(r"(.+?)(\d+)",v),(m.group(1).lower(),int(m.group(2)))][1])
"""
