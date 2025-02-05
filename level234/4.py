"""이중우선순위큐

구현할때
만약 아이템들의 중복을 허용한다면
del_set이 아니라
del_dict로 구현해야함.

"""

import heapq as h
from collections import defaultdict


class Heap:
    def __init__(self, iterable=[], mode="min"):
        self.ls = list(iterable)
        h.heapify(self.ls)

        self.mode = 1 if mode == "min" else -1

        self.del_dict = defaultdict(int)

    def top(self):
        return self.mode * self.ls[0]

    def pop(self):
        value = self.mode * h.heappop(self.ls)

        while self and self.top() in self.del_dict:
            self.del_dict[self.top()] -= 1
            if self.del_dict[self.top()] == 0:
                del self.del_dict[self.top()]

            h.heappop(self.ls)

        return value

    def push(self, value):
        h.heappush(self.ls, self.mode * value)

    def remove(self, value):
        if self.top() == value:
            self.pop()
        else:
            self.del_dict[value] += 1

    def __bool__(self):
        return bool(self.ls)


def solution(operations):
    min_heap = Heap()
    max_heap = Heap(mode="max")

    for operation in operations:
        op, num = operation.split(" ")
        num = int(num)

        if op == "I":
            min_heap.push(num)
            max_heap.push(num)
        elif num == 1:  # D 1 -> 최댓값 삭제
            if not max_heap:
                continue
            max_value = max_heap.pop()
            min_heap.remove(max_value)
        else:  # D -1 -> 최솟값 삭제
            if not min_heap:
                continue
            min_value = min_heap.pop()
            max_heap.remove(min_value)

    if not min_heap:
        return [0, 0]

    return [max_heap.top(), min_heap.top()]
