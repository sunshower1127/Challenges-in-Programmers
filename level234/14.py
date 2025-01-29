"""[카카오 인턴] 보석 쇼핑

슬라이딩 윈도우 그거 아닌가요

"""

from collections import defaultdict


def solution(gems):
    counter = defaultdict(int)
    target_len = len(set(gems))
    shortest = [0, 100000]

    start = 0
    for end, gem in enumerate(gems):
        counter[gem] += 1

        if len(counter) == target_len:
            while counter[gems[start]] > 1:
                counter[gems[start]] -= 1
                start += 1

            if end - start < shortest[1] - shortest[0]:
                shortest = [start, end]

    return [shortest[0] + 1, shortest[1] + 1]
