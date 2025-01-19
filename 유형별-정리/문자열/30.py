"""[1차] 뉴스 클러스터링

고급 정규식이 들어갔음.
정규식이 더 어려우므로 문자열로 들어감
"""

import re
from collections import Counter


def solution(str1, str2):
    pattern = re.compile(r"(?=([a-z]{2}))[a-z]")

    counter1 = Counter(pattern.findall(str1.lower()))
    counter2 = Counter(pattern.findall(str2.lower()))

    union = counter1 | counter2
    intersection = counter1 & counter2

    if not union:
        return 65536

    return 65536 * sum(intersection.values()) // sum(union.values())
