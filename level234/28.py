"""풍선 터뜨리기

인접한 두 풍선을 골라서
하나를 터뜨리고
빈공간을 메꿔야함.
번호가 더 작은 풍선을 터뜨리는건 -> 최대 1번
최후까지 남길 수 있는 풍선의 경우의 수는?

10^6 개

보통은 큰걸 터뜨린다라는거죠
그러면 최솟값이 원래 남아야하는데,
한 번은 더 작은걸 터뜨릴 수 있다?

흠

모르겠어요

간단하게 생각해보자 이거죠

어차피 다 터져
그쵸

왼쪽에서 제일 큰값 남고
오른쪽에서 제일 큰값 남음.

왼쪽 값, v, 오른쪽 값

여기서, v가 제일 작으면 바이바이임.

빼고 싶은건 자유롭게 다 빼면서
최댓값을 남긴다라...
작은거를 남겨야함.

3 1 3

이면

안정적이죠

1 2 3

이것도 안정적이겠지 뭐

중요한건

가운데가 제일 크지만 않으면 됨.

중간 삭제 가능한 최소/최대힙은 무조건 class로 구현하는게 좋음.
잘 외워두자.


"""

import heapq as h


class MinHeap:
    def __init__(self, iterable):
        self.ls = list(iterable)
        h.heapify(self.ls)

        self.del_set = set()

    def top(self):
        return self.ls[0]

    def __bool__(self):
        return bool(self.ls)

    def pop(self):
        min_v = h.heappop(self.ls)

        while self.top() in self.del_set:
            self.del_set.remove(h.heappop(self.ls))

        return min_v

    def push(self, value):
        h.heappush(self.ls, value)

    def remove(self, value):
        if value == self.top():
            self.pop()
        else:
            self.del_set.add(value)


def solution(a):
    left_min_v = float("inf")
    right_min_heap = MinHeap(a)
    cnt = 0

    for i in range(len(a) - 1):
        mid = a[i]
        right_min_heap.remove(mid)

        right_min_v = right_min_heap.top()

        if mid > left_min_v and mid > right_min_v:
            cnt += 1

        left_min_v = min(left_min_v, mid)

    return len(a) - cnt
