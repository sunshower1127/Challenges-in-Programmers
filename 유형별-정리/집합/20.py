"""

할인 행사

want ["banana", "apple"]
number [3, 2]
이면
banana 3개, apple 2개를 사야한다는 뜻이다.

discount엔 날짜별로 할인 하는 품목이 하나씩 써져있다.

discount에서 10일연속으로 딱 꺼냈을때, 원하는 품목과 개수가 모두 들어있다면 cnt+1
해서 cnt를 구해보자.

tip : 이렇게 연속된 부분을 이동하면서 합을 구하는 문제는 복잡도를 생각한다면 투포인터가 낫다.

근데 여기서 Counter 시간복잡도가 좀 의심되네

"""

from collections import Counter as cnter


def solution(want, number, discount):
    Dict = dict(zip(want, number))

    Cnt = 0
    Cnter = cnter(discount[:10])

    if Cnter == Dict:
        Cnt += 1

    for i in range(10, len(discount)):
        Cnter[discount[i - 10]] -= 1
        if Cnter[discount[i - 10]] == 0:
            del Cnter[discount[i - 10]]

        Cnter[discount[i]] += 1

        if Cnter == Dict:
            Cnt += 1

    return Cnt
