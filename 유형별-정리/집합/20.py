"""XYZ 마트

어쩌다보니 dict 총 정리가 되버림

"""

from collections import Counter, defaultdict


def dict_diff(dict_a, dict_b):
    keys = {*dict_a.keys()} | {*dict_b.keys()}

    dict_c = {}
    for key in keys:
        value = dict_a.get(key, 0) - dict_b.get(key, 0)
        if value != 0:
            dict_c[key] = value

    return dict_c


def update_dict_value(dic, key, v):
    dic[key] += v
    if dic[key] == 0:
        del dic[key]


def solution(want, number, discount):
    result = 0
    items_to_buy = []
    for name, num in zip(want, number):
        items_to_buy += [name] * num

    wanted_counter = Counter(items_to_buy)

    discount_counter = Counter(discount[:10])

    missing = dict_diff(discount_counter, wanted_counter)
    missing = defaultdict(int, missing)

    if not missing:
        result += 1

    for i in range(1, len(discount) - 10 + 1):
        old_one = discount[i - 1]
        new_one = discount[i + 9]

        update_dict_value(missing, old_one, -1)
        update_dict_value(missing, new_one, 1)

        if not missing:
            result += 1

    return result
