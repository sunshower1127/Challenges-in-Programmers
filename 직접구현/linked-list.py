class Node:
    def __init__(self, item):
        self.item = item
        self.prev: Node | None = None
        self.next: Node | None = None


class Deque:
    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.size = 0
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def append(self, item):
        new_node = Node(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendleft(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.tail is None:
            raise IndexError("pop from an empty deque")

        item = self.tail.item
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return item

    def popleft(self):
        if self.head is None:
            raise IndexError("pop from an empty deque")

        item = self.head.item
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return item

    def __len__(self):
        return self.size

    def __bool__(self):
        return bool(self.size)

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.item
            current = current.next

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("인덱스는 정수여야 합니다")

        if self.size == 0:
            raise IndexError("빈 deque입니다")

        # 음수 인덱스 처리
        if index < 0:
            index = self.size + index

        if not (0 <= index < self.size):
            raise IndexError("인덱스가 범위를 벗어났습니다")

        # 인덱스가 전체 크기의 절반보다 작으면 앞에서부터 탐색
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        # 크면 뒤에서부터 탐색
        else:
            current = self.tail
            for _ in range(self.size - 1 - index):
                current = current.prev

        return current.item

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError("인덱스는 정수여야 합니다")

        if self.size == 0:
            raise IndexError("빈 deque입니다")

        # 음수 인덱스 처리
        if index < 0:
            index = self.size + index

        if not (0 <= index < self.size):
            raise IndexError("인덱스가 범위를 벗어났습니다")

        # 인덱스가 전체 크기의 절반보다 작으면 앞에서부터 탐색
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        # 크면 뒤에서부터 탐색
        else:
            current = self.tail
            for _ in range(self.size - 1 - index):
                current = current.prev

        current.item = value


deque = Deque([1, 2, 3, 4, 5])
deque.appendleft(123)
deque.pop()
deque.append(4)
print(*deque)  # 1
