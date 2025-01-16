"""

두 큐 합 같게 만들기

코테에서는 복잡한 알고리즘을 요구하지 않음 -> 그냥 직관적인 그리디 문제일 가능성이 크다.

이것도 두 큐의 합을 같게 만들기인데,
복잡하게 생각하면 경우의 수 하나하나 트리 탐색하면서, 복잡한 조건 걸어서 브랜치 쳐내야하는걸로 생각할 수 있지만,
그정도 레벨은 코테에서 나오지 않으므로,
간단하게 그냥 값이 큰쪽에서 작은쪽으로 계속 주면 되지않을까? 생각하면됨.
그리디겠지 뭐~ -> 정답

종료 조건은 이제 한쪽이 텅비어버렸을때임. 근데 잘 생각이 안난다면 그냥 큰값으로 설정하자.
AI는 큐의 길이 * 3으로 cnt를 제한했는데, 무슨 원리인지는 잘 모르겠음
"""

from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    targetnum = (sum1 + sum2) // 2

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    for cnt in range(1, 10**7):
        if sum1 == targetnum:
            return cnt - 1
        elif sum1 > targetnum:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum2 -= num
            sum1 += num

    return -1
