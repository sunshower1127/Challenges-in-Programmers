"""이중우선순위큐
우선순위?큐?

암튼 이중힙임

원리는

최소힙하고 최대힙을 동시에 돌리는데

삭제된 애를 근데 어떻게 처리하지

그냥 remove해도 시간초과 안되네 나이스

"""

from heapq import heappop, heappush


def solution(operations):
    max_heap = []
    min_heap = []

    for operation in operations:
        op, num = operation.split(" ")
        num = int(num)

        if op == "I":
            heappush(max_heap, -num)
            heappush(min_heap, num)
        elif max_heap:  # D
            if num == 1:
                max_v = -heappop(max_heap)
                min_heap.remove(max_v)
            else:  # -1
                min_v = heappop(min_heap)
                max_heap.remove(-min_v)

    max_v = -heappop(max_heap) if max_heap else 0
    min_v = heappop(min_heap) if min_heap else 0

    return [max_v, min_v]
