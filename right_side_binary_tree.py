'''
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
'''


def height(arr, node):
    if node >= len(arr):
        return 0
    if arr[node] is None:
        return 0
    l_height = height(arr, 2*node + 1)
    r_height = height(arr, 2*node + 2)
    return max(l_height, r_height) + 1


def traverse_given_level(arr, node, level):
    if node >= len(arr) or arr[node] is None:
        return
    if level == 0:
        print(arr[node])
    elif level >= 1:
        traverse_given_level(arr, node * 2 + 1, level - 1)
        traverse_given_level(arr, node * 2 + 2, level - 1)


def level_order_traversal(arr):
    h = height(arr, 0)
    for i in range(h):
        traverse_given_level(arr, 0, i)


def queue_based_level_order_traversal(arr):
    queue = []
    queue.append(0)
    while len(queue) > 0:
        print(arr[queue[0]])
        temp = queue.pop(0)
        if 2 * temp + 1 < len(arr) and arr[2 * temp + 1] is not None:
            queue.append(2 * temp + 1)
        if 2 * temp + 2 < len(arr) and arr[2 * temp + 2] is not None:
            queue.append(2 * temp + 2)


def right_tree_view(arr, node, level, max_level):
    if node >= len(arr) or arr[node] is None:
        return

    if max_level[0] < level:
        print(arr[node])
        max_level[0] = level

    right_tree_view(arr, 2 * node + 2, level + 1, max_level)
    right_tree_view(arr, 2 * node + 1, level + 1, max_level)


if __name__ == '__main__':
    input = [1, 2, 3, 4, 5, 7, None, None, None, 6]
    # level_order_traversal(input)
    # queue_based_level_order_traversal(input)
    root = 0
    level = 1
    max_level = [0]
    right_tree_view(input, root, level, max_level)
