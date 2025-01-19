"""듀 큐 합 같게 만들기

3 2 7 2
4 6 5 1

15 15로 만들어야함.
뭐부터 뺼거임?
합이 큰거부터요

이게 그리디거든~ 모르겠고~ 일단 때려 맞춰보기~

"""

from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    target_sum = (sum1 + sum2) // 2

    cnt = 0
    length = len(queue1) + len(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while sum1 != target_sum:
        if sum1 > target_sum:
            item = queue1.popleft()
            queue2.append(item)
            sum1 -= item
            sum2 += item
        else:
            item = queue2.popleft()
            queue1.append(item)
            sum2 -= item
            sum1 += item
        cnt += 1
        if cnt > 2 * length:
            return -1

    return cnt
