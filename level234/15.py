"""징검다리 건너기


200_000개

몇명이 건널 수 있음?
1씩 계속 뺐을때
0인 것의 길이가 k이상이면 리턴.

근데 10*5고,
그냥 n이면 누가봐도 시간초과인데

1~n 이하인 수가 k개 이상 나열되어있는가 인가

최소가 중요한거죠
minheap인거 같은데
근데 이게 중간에 아무거나 삭제해야해서
heapify를 해줘야하는데?

그냥 큐로 구현해도 괜찮을드

최적화를 해야하는데
매번 max를 구하면 안됨

입출력이 자유로운 max_heap?
이진 트리?
그냥 counter도 같이 돌려서
삭제하면? -> 삭제 counter에 추가함
이게 맞지않나요

"""

from collections import defaultdict
from heapq import heapify, heappop, heappush
from operator import neg


def pop_all(heap, delete_cnt):
    while heap and -heap[0] in delete_cnt:
        delete_cnt[-heap[0]] -= 1
        if delete_cnt[-heap[0]] == 0:
            del delete_cnt[-heap[0]]

        heappop(heap)


def solution(stones, k):
    max_heap = list(map(neg, stones[:k]))

    heapify(max_heap)

    min_v = -max_heap[0]

    delete_cnt = defaultdict(int)

    for i in range(k, len(stones)):
        old_i = i - k

        old_v = stones[old_i]

        delete_cnt[old_v] += 1
        pop_all(max_heap, delete_cnt)

        heappush(max_heap, -stones[i])

        min_v = min(min_v, -max_heap[0])

    return min_v

"""
이진 탐색으로 푸는 방법도 있다고함
솔직히 이해 못했음 어떻게 푸는거야
암튼 있다는 것만 알아두자
"""

def solution2(stones, k):
    left = 1
    right = max(stones)

    def can_cross(mid):
        count = 0  # 연속된 0 이하의 돌 개수
        for stone in stones:
            if stone - mid <= 0:
                count += 1
            else:
                count = 0
            if count >= k:
                return False
        return True

    # 이진 탐색
    while left <= right:
        mid = (left + right) // 2
        if can_cross(mid):
            left = mid + 1
        else:
            right = mid - 1

    return right
