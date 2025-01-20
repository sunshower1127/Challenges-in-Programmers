"""heap

heap은 트리에서 노드의 높이가 높을수록 값이 크거나 작아짐.
최대힙이면 루트가 제일 크겠죠. 그 아래 레벨들이 2번째겠고,

자식은? *2 +1, +2
부모는? -1 // 2
사실 이것만 알면 뭐

삭제는 당연히 루트에서만 가능하구요 삭제한 자리를 이제 맨 끝 노드로 대체하고 그 노드를 내리면 됩니다.
추가는 맨 끝에 놓고 올리면 됨.

생각보다 별건 없죠

"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return min_val

    def _sift_down(self, i):
        min_idx = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
            min_idx = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
            min_idx = right

        if i != min_idx:
            self.swap(i, min_idx)
            self._sift_down(min_idx)
