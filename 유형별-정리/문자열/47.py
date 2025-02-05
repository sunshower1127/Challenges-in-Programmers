"""[3차] 파일명 정렬"""

import re


def get_key(v):
    match = re.match(r"(.+?)([0-9]+)", v)
    assert match
    return (match.group(1).lower(), int(match.group(2)))


def solution(files):
    files.sort(key=get_key)
    return files
