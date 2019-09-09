class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node):
        if self is None:
            self = node
        else:
            if self.data < node.data:
                if self.right is None:
                    self.right = node
                else:
                    self.right.insert(node)
            else:
                if self.left is None:
                    self.left = node
                else:
                    self.left.insert(node)

    def traverse(self):
        if not self is None:
            if not self.left is None:
                self.left.traverse()
            print(self.data)
            if not self.right is None:
                self.right.traverse()

class BSTIterator:

    def __init__(self, root):
        self.root = root
        self.current = root
        while not self.current.left is None:
            self.current = self.current.left

    def next(self):
        if not self.current.right is None:
            temp = self.current.right
            while not temp.left is None:
                temp = temp.left
            return temp.data
        else:
            temp = root
            successor = None
            while not temp is None:
                if self.current.data < temp.data:
                    successor = temp
                    temp = temp.left
                elif self.current.data > temp.data:
                    temp = temp.right
                else:
                    break
            self.current = successor
            return successor


if __name__ == '__main__':
    root = Node(10)
    root.insert(Node(3))
    root.insert(Node(20))
    root.insert(Node(50))
    root.insert(Node(1))
    root.insert(Node(23))
    root.traverse()

    iterator = BSTIterator(root)
    print('--', iterator.next().data)
    print('--', iterator.next().data)
    print('--', iterator.next().data)
