"""

주식가격

prices는 시간에 따른 주식 가격임.

각 price마다 자신 이후로 몇초동안 값이 자신의 값 이상이었는지를 반환.

예)
prices = [1, 2, 3, 2, 3]

return = [4, 3, 1, 1, 0]

바로 다음에 떨어지면 1초임.

길이는 10^5. -> O(n^2)은 안됨.

난 이런 스택류 문제 머리아파서 못풀겠음

스택류 문제는 거꾸로 푸는게 아니라 스택에 저장해서 처리한다는 점에서 dp하고 결이 비슷한듯.

그러니깐 스택문제 = 중복처리를 어떻게 할것인가 인듯

i로 쭉 훑는데, 오른쪽 나머지 애들을 계속 계산해야함 -> 계속해서 중복이 일어남. -> O(n^2)
-> i로 쭉 훑는데, Stack에 저장해가면서 훑음 -> O(n * Stack길이)로 압축 가능

namedtuple 한 번 써봤는데 어떤지 모르겠네
괜찮은거 같기도 하죠

"""

from collections import deque, namedtuple


def solution(prices):
    Tuple = namedtuple("Tuple", "i Price")
    N = len(prices)
    Stack = deque()
    Result = [0] * N

    for i, Price in enumerate(prices):

        while Stack and Stack[-1].Price > Price:
            Result[Stack[-1].i] = i - Stack[-1].i
            Stack.pop()

        Stack.append(Tuple(i=i, Price=Price))

    while Stack:
        Result[Stack[-1][0]] = N - 1 - Stack[-1][0]
        Stack.pop()

    return Result
