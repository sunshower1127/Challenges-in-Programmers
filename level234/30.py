"""순위

비효율적인거 같아도
그냥 전부 나열하면 됨.

weakers
1 2
2 5
3 2
4 3 2
5

strongers
1
2 1 3
3 4
4
5 2

4 > 3 > 2 > 5
    1

이건 어렵네요
그냥 외우는게 나을듯.
기준되는 노드가 있을때
자기보다 약한애들, 자기보다 강한애들 집합을 만들고
자기보다 강한애는 당연히 자기보다 약한애들을 포함시켜야하니깐
이런 논리대로 한 번 for문 돌면
모든 정보를 알 수 있음.
"""


def solution(n, results):
    strongers = [set() for _ in range(n + 1)]
    weakers = [set() for _ in range(n + 1)]

    for winner, loser in results:
        weakers[winner].add(loser)
        strongers[loser].add(winner)

    for i in range(1, n + 1):
        for stronger in strongers[i]:
            weakers[stronger] |= weakers[i]
            # i가 있고, i보다 쌘애가 있는데, i보다 약한애들은 i보다 쌘애의 약한애들임.

        for weaker in weakers[i]:
            strongers[weaker] |= strongers[i]
            # i가 있고, i보다 약한애가 있는데, i보다 강한애들은 i보다 약한애의 쌘애들임.

    return [
        len(weaker) + len(stronger) == n - 1
        for weaker, stronger in zip(weakers, strongers)
    ].count(True)
