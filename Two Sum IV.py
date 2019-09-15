
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.arr = []


    def in_order_traversal(self, root):
        if root is not None:
            self.in_order_traversal(root.left)
            self.arr.append(root.val)
            self.in_order_traversal(root.right)

    def binary_search(self, left, right, val):
        if right >= left:
            mid = left + int((right - left)/2)
            if self.arr[mid] == val:
                return mid
            if self.arr[mid] > val:
                return self.binary_search(left, mid - 1, val)
            else:
                return self.binary_search(mid + 1, right, val)
        else:
            return -1


    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.in_order_traversal(root)
        print(self.arr)
        l = len(self.arr)
        for i in range(l-1):
            res = self.binary_search(i+1, l - 1, k - self.arr[i])
            if res != -1:
                return True
        return False


if __name__ == '__main__':
    tree_node = TreeNode(2)
    tree_node.left = TreeNode(1)
    tree_node.right = TreeNode(3)

    sol = Solution()
    res = sol.findTarget(tree_node, 4)
    print(res)
