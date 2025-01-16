"""

구명 보트

보트에 최대 2명

limit 이하의 무게 합

최소 몇개 보트 필요?

70 50 80 50 -> 70 / 80 / 50 50 -> 3개

tip : 이게 좀 직관적이지 않은 그리디 문제임. 최대한 효율적으로 낭비없이 넣어보자.

"""


def solution(people, limit):
    people.sort()

    Left = 0
    Right = len(people) - 1
    Cnt = 0
    while True:
        if Left == Right:
            Cnt += 1
            return Cnt

        if Left > Right:
            return Cnt

        if people[Left] + people[Right] > limit:
            Cnt += 1
            Right -= 1
            continue

        Left += 1
        Right -= 1
        Cnt += 1
