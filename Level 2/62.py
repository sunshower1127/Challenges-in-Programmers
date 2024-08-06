"""

시소 짝꿍

소수판단이라서, 흠. 그냥 곱셈으로 판단하지뭐
1
2/3
1/2
3/2
1
3/4
2/1
4/3
1

정렬같은걸 하나? 굳
100 100 180 270 360
이러면 찾을때 bisect 쓸 수 있고,
오른쪽에서만 자기보다 같거나 큰거 찾으면 됨
bisect가 아니라 counter를 쓴다면?

아 이런 디테일들이...
어렵네요 문제가...
뭐 어디서부터 잘못된건지도 모르겠네.....
"""

from collections import Counter


def solution(weights):
    cnter = Counter(weights)
    result = 0

    for key in cnter:
        if cnter[key] >= 2:
            result += cnter[key] * (cnter[key] - 1) // 2

        if (key * 3) % 2 == 0 and (key * 3 // 2) in cnter:
            result += cnter[key] * cnter[key * 3 // 2]

        if (key * 4) % 3 == 0 and (key * 4 // 3) in cnter:
            result += cnter[key] * cnter[key * 4 // 3]

        if (key * 2) in cnter:
            result += cnter[key] * cnter[key * 2]

    return result


def solution_ai(weights):
    cnter = Counter(weights)
    result = 0

    for key in cnter:
        count = cnter[key]

        # 같은 무게끼리의 짝꿍
        if count >= 2:
            result += count * (count - 1) // 2

        # 다른 무게끼리의 짝꿍
        for factor in [3 / 2, 4 / 3, 2]:
            target = key * factor
            if target in cnter:
                result += count * cnter[target]

    return result
