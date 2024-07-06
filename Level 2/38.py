"""

롤케이크 자르기

리스트를 두도막 냄.

그때 각각의 리스트에 담긴 숫자의 종류의 개수가 같은 경우의 수 리턴.

리스트의 길이가 10^6임.

일단 자르는게 O(n)이고,

자를때마다 세면 시간복잡도 초과니깐 하나씩만 변경하는게 맞겠죠.

개수를 미리 count해놓는 dict가 필요 -> Counter

Counter 하나씩 더하고 뺄때,

1. Counter -= counter([원소])
이건 O(n)이고

2. Counter[원소] -= 1
if Counter[원소] == 0 : del Counter[원소]
이건 O(1)임.
무조건 아래를 쓰자.

정리하자면
1. Counter에서 하나씩 더하고 뺄때는 직접 원소에 접근하자.
2. 근데 직접 접근하면 0이 됐을때 삭제가 안되므로 if del 추가 로직 필요.

"""

from collections import Counter as counter


def solution(topping):
    Cnt = 0
    LeftCounter = counter()
    RightCounter = counter(topping)
    for i, Each in enumerate(topping):
        if Each not in LeftCounter:
            LeftCounter[Each] = 0
        LeftCounter[Each] += 1

        RightCounter[Each] -= 1
        if RightCounter[Each] == 0:
            del RightCounter[Each]

        if len(LeftCounter) == len(RightCounter):
            Cnt += 1

    return Cnt
