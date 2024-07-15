"""

프로세스

우선순위 큐 구현

1. 큐에서 프로세스 하나를 꺼냄
2. 큐의 나머지 프로세스들과 비교함
    -> 만약 큐의 나머지 프로세스들 중에 현재 프로세스보다
        우선순위가 높은 프로세스가 있다면 다시 큐에 넣음

location의 index의 프로세스가 몇번째로 처리되는지 반환

"""

from collections import deque


def solution(priorities, location):
    Queue = deque(enumerate(priorities))

    Num = 1
    while True:
        Cur = Queue.popleft()

        Break = False

        for Each in Queue:
            if Each[1] > Cur[1]:
                Break = True
                break

        if Break:
            Queue.append(Cur)
        else:
            if Cur[0] == location:
                return Num

            Num += 1
