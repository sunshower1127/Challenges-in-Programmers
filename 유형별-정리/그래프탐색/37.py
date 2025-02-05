"""모음사전

일단 앞자리부터 비교함.
짧은게 더 먼저.
길이 1인게 5개
2인게 5^2
5+ 25 + 125 + 625 + 3125 그냥 사전을 만들라 이거네요

4000이니깐 정렬해도 될듯?

A
AA
AAA
AAAA
AAAAA
AAAAE
AAAAI
AAAAO
AAAAU
AAAE
AAAEA
AAAEE
AAAEI
AAAEO
AAAEU
AAAI
...
UUUUU

product에다가 Boolean 넣기 -> 비트연산 대체 가능
product repeat i 넣기 -> dfs로 대체 가능

"""

from itertools import product


def solution1(word):
    dictionary = []
    for i in range(1, 6):
        dictionary += ["".join(tp) for tp in product("AEIOU", repeat=i)]

    dictionary.sort()
    return dictionary.index(word) + 1


def solution2(word):
    stack = []
    stack.append([])
    dictionary = []

    while stack:
        path = stack.pop()
        dictionary.append("".join(path))

        if len(path) == 5:
            continue

        for c in reversed("AEIOU"):
            stack.append([*path, c])

    left, right = 0, len(dictionary)
    while left <= right:
        mid = (left + right) // 2
        if dictionary[mid] == word:
            return mid
        if dictionary[mid] < word:
            left = mid + 1
        else:
            right = mid - 1

    return None
