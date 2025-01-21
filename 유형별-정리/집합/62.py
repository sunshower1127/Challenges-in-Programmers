"""시소 짝꿍

nC2 시간초과니깐

일단 정렬하고

표본이 900개임. 길이는 100000개.
100개씩 겹친다는거죠. Counting sort로 갑시다.

2 3 4

2 3 -> 1.5

1 2 -> 2

3 4 -> 1.25

1.25, 1.5, 2

1/2 2/3 3/4

일단 이게 컨셉이

100 180 270 360

[100] 180 일때 이제 계산. 엥 없네 넣어
[100 180] 270 계산. 100은 1/2 보다 작으니깐 삭제. 180은 result에 추가.
[180 270] 360. 180 안에있는거 다 되니깐 추가추가.
앞에 있는걸 삭제해야하니깐 거꾸로 탐색.

reversed(enumerate())는 안됨. 그렇다면? 그냥 range를 쓰던가 아예 자료구조 설계를 거꾸로 하던가..
그리고 실수는 항상 조심하자. 실수 나눗셈은 최대한 지양하셈

투포인터 문제였는데, 투포인터는 사회악임 그냥.
투포인터는 스택이나 큐로 과거 애들을 저장하는 식으로 최적화를 할 수 있다.

"""

from collections import Counter, deque


def pop_right(q, i):
    for _ in range(i, len(q)):
        q.pop()


def solution(weights):
    counter = Counter(weights)

    sorted_items = sorted(counter.items())

    result = 0
    q = deque()

    for weight, cnt in sorted_items:
        if cnt > 1:
            result += cnt * (cnt - 1) // 2

        for i, (q_weight, q_cnt) in enumerate(q):
            if q_weight * 2 < weight:
                pop_right(q, i)
                break
            if (
                2 * q_weight == weight
                or 3 * q_weight == 2 * weight
                or 4 * q_weight == 3 * weight
            ):
                result += cnt * q_cnt
        q.appendleft((weight, cnt))
    return result
