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

from collections import Counter as cnter


def solution(topping):
    Cnt = 0
    LeftCnter = cnter()
    RightCnter = cnter(topping)
    for Each in topping:
        if Each not in LeftCnter:
            LeftCnter[Each] = 0
        LeftCnter[Each] += 1

        RightCnter[Each] -= 1
        if RightCnter[Each] == 0:
            del RightCnter[Each]

        if len(LeftCnter) == len(RightCnter):
            Cnt += 1

    return Cnt


"""

for i in range(1, 7) -> 숫자 지정 가능.
for i in range(len(Something))
for Each in Something -> 위보다 직관적이고 짧은 코드.
for i, _ in enumerate(Something) -> index만 필요할때.
for _, Each in enumerate(Something) -> index가 필요없을때.

무슨 방법이 우월하다 그런건 없음. 다 장점이 있고 단점이 있어서

dp는 for i in range()를 반드시 써야하고
일반적인 상황에선 뭐 for i in range가 맞긴한데
복잡할때 Each가 주는 간소함도 무시할 수 없어서
상황따라 쓰면 됩니다. 고민하는 시간도 아까움.

"""
