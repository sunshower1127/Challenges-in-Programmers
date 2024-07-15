"""

택배상자

택배박스를 n개 실어야하는데,
1~n까지 순서대로 번호가 붙어있음.
택배기사가 order한 순서대로 넣어야하지만,
큐라서 어쩔 수 없으니깐 예비 스택을 하나더 만들어서 거따 쌓아놓음.
큐에서 가져오거나 스택에서 가져와서 순서를 맞추는데
못넣겠으면 지금까지 넣은 택배박스 수 리턴하면 됨.
근데 구지 큐를 구현할 필요가 있나 어차피 for문 쓰면 그게 큐인데

"""

from collections import deque


def solution(order):
    N = len(order)
    Stack = deque()
    Queue = deque(range(1, N + 1))
    Result = 0

    for Num in order:
        if Queue and Num == Queue[0]:
            Queue.popleft()
            Result += 1
        elif Queue and Num > Queue[0]:
            while Num > Queue[0]:
                Stack.append(Queue.popleft())

            Queue.popleft()
            Result += 1

        else:
            if Stack and Num == Stack[-1]:
                Stack.pop()
                Result += 1
            else:
                return Result

    return Result
