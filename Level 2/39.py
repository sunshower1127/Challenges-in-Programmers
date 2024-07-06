"""

뒤에 있는 큰 수 찾기

리스트가 있음.

자기보다 뒤에 있으면서 자기보다 큰 수 중에서 제일 가까운 수
-> 뒷 큰수
없으면 -1

길이가 10^6임. 하..

이런 류의 문제는 보통 stack, queue 아니면 dp임.

이런 문제 개인적으로 암기류라서 좋아하지는 않는데

거꾸로 풀어봤자 의미 없는거 같고

그래프 관점에서 생각했을때 홈 메꾸기 거든요

암튼 그냥 스택 집어넣어. 이거 머리아파. 그냥 암기야

"""

from collections import deque


def solution(numbers):
    N = len(numbers)
    Result = [-1] * N
    Stack = deque()
    for i in range(N):

        while Stack and numbers[Stack[-1]] < numbers[i]:
            Result[Stack.pop()] = numbers[i]

        Stack.append(i)

    return Result
