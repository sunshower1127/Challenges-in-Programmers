"""더 맵게

K이상으로!

오호라

섞어야 하는 최소 횟수라

직접 MinHeap을 구현해봤지만
시간초과 나옴
...

python으로 heap을 구현해봤자 구리다..
c로 구현된 heapq를 쓰자..
"""


class MinHeap:
    def __init__(self, iterable=None):
        self.heap = []

        if not iterable:
            return

        for item in iterable:
            self.push(item)

    def push(self, item):
        self.heap.append(item)
        self._sift_up(len(self) - 1)

    def pop(self):
        min_v = self[0]
        self[0] = self[-1]
        self.heap.pop()
        self._sift_down(0)
        return min_v

    def _sift_up(self, i):
        if i == 0:
            return

        parent_i = (i - 1) // 2

        if self[i] < self[parent_i]:
            self[i], self[parent_i] = self[parent_i], self[i]
            self._sift_up(parent_i)

    def _sift_down(self, i):
        child1_i = i * 2 + 1
        child2_i = i * 2 + 2

        if child1_i < len(self) and self[i] > self[child1_i]:
            if child2_i < len(self) and self[child1_i] > self[child2_i]:
                self[i], self[child2_i] = self[child2_i], self[i]
                self._sift_down(child2_i)
            else:
                self[i], self[child1_i] = self[child1_i], self[i]
                self._sift_down(child1_i)

        elif child2_i < len(self) and self[i] > self[child2_i]:
            if child1_i < len(self) and self[child2_i] > self[child1_i]:
                self[i], self[child1_i] = self[child1_i], self[i]
                self._sift_down(child1_i)
            else:
                self[i], self[child2_i] = self[child2_i], self[i]
                self._sift_down(child2_i)

    def __getitem__(self, i):
        return self.heap[i]

    def __setitem__(self, i, value):
        self.heap[i] = value

    def __bool__(self):
        return bool(self.heap)

    def __len__(self):
        return len(self.heap)


def solution(scoville, K):
    min_heap = MinHeap(scoville)
    cnt = 0
    while True:
        min1 = min_heap.pop()
        if min1 >= K:
            return cnt

        if not min_heap:
            return -1

        min2 = min_heap.pop()

        min_heap.push(min1 + min2 * 2)

        cnt += 1
