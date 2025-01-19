"""튜플

중복가능
순서 존재

n개의 중복없는 튜플이 주어질때

2, 1, 3, 4가 주어지면
2, 21, 213, 2134

아 일단 그래서 nested된 원소, 어떻게 읽어들일건지?


"""

import re


def solution(s):
    set_list = []
    for set_str in re.findall(r"(?<=\{)([\d,]+?)(?=\})", s):
        new_set = set(map(int, set_str.split(",")))
        set_list.append(new_set)

    set_list.sort(key=len)
    result = []
    mem = set()
    for num_set in set_list:
        result.append(next(iter(num_set - mem)))
        mem = num_set

    return result
