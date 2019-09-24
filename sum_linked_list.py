class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_next(self, node):
        self.next = node

def sum(node_a, node_b):
    node_sum = None
    carry = 0
    start_node = None
    while node_a is not None or node_b is not None:
        s = carry
        if node_a is not None:
            s = node_a.value
        if node_b is not None:
            s += node_b.value
        temp = None
        if s >= 10:
            temp = Node(s%10)
            carry = 1
        else:
            temp = Node(s)
            start_node = temp
            carry = 0

        if node_sum is None:
            node_sum = temp
        else:
            temp.add_next(node_sum)
            node_sum = temp
        if node_a is not None:
            node_a = node_a.next
        if node_b is not None:
            node_b = node_b.next
            
    return node_sum


if __name__ == '__main__':
    node_a = Node(6)
    node_a.next = Node(5)
    node_a.next.next = Node(4)

    node_b = Node(8)
    node_b.next = Node(7)
    node_b.next.next = Node(3)
    node_b.next.next.next = Node(3)

    node_sum = sum(node_a, node_b)
    while node_sum is not None:
        print(node_sum.value)
        node_sum = node_sum.next
