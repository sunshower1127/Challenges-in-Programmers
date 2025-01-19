"""구명보트

2명씩

무게제한이 존재함.

최소한의?

이러면 가장 무거운 애를 가장 가벼운 애하고 데리고 갈 수 있나? 가 관건인듯
그리디죠

deque은 sort가 없구나

"""

from collections import deque


def solution(people, limit):
    people.sort()
    people = deque(people)
    cnt = 0
    while people:
        heaviest = people.pop()
        if len(people) >= 1 and heaviest + people[0] <= limit:
            people.popleft()

        cnt += 1

    return cnt
