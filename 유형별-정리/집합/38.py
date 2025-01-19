"""롤케이크 자르기

잘랐을때 종류가 같아야함.

양쪽에 set을 놓으면 되겠죠
안되네 counter로 가야됨.

"""

from collections import Counter, defaultdict


def increment(dic, key):
    dic[key] += 1


def decrement(dic, key):
    dic[key] -= 1
    if dic[key] == 0:
        del dic[key]


def solution(toppings):
    left = defaultdict(int)
    right = defaultdict(int, Counter(toppings))

    result = 0
    for topping in toppings:
        increment(left, topping)
        decrement(right, topping)
        if len(left) == len(right):
            result += 1

    return result
