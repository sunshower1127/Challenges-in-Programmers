"""문자열 압축


음. 순서가 섞이지 않는 카운터라...

아이디어를 생각해봅시다
투포인터는 굉장히 복잡해질 수 있기때문에

배열을 계속 변경하는 방식으로 가는게 맞음.

일단 사실 여기서 re하고 reduce 다 필요없었음.
너무 겉멋이 든거 같기도 하고...
"""

import re
from functools import reduce


def combine_consecutive(result, current_str):
    if not result or current_str != result[-1][0]:
        result.append([current_str, 1])
    else:
        result[-1][1] += 1

    return result


def solution(s):
    min_length = float("inf")

    for length in range(1, len(s) + 1):
        chunks = re.findall(".{1," + str(length) + "}", s)

        compressed = reduce(combine_consecutive, chunks, [])

        compressed_str = "".join(
            f"{cnt if cnt > 1 else ''}{word}" for word, cnt in compressed
        )

        min_length = min(min_length, len(compressed_str))

    return min_length
