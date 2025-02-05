class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:  # noqa: PLR5501
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def delete(self, key):
        self.root = self._delete_rec(self.root, key)

    def _delete_rec(self, node, key):
        if node is None:
            return node
        if key < node.value:
            node.left = self._delete_rec(node.left, key)
        elif key > node.value:
            node.right = self._delete_rec(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # 오른쪽 서브트리의 가장 왼쪽 노드값을 뜯어옴.
            temp = self._min_value_node(node.right)
            node.value = temp.value
            node.right = self._delete_rec(node.right, temp.value)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, key):
        return self._find_rec(self.root, key)

    def _find_rec(self, node, key):
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._find_rec(node.left, key)
        return self._find_rec(node.right, key)

    def traverse(self):
        return self._traverse_in_order(self.root)

    def _traverse_in_order(self, node):
        res = []
        if node:
            res = self._traverse_in_order(node.left)
            res.append(node.value)
            res = res + self._traverse_in_order(node.right)
        return res
