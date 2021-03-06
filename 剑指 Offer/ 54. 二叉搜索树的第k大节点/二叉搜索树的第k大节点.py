# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        count = 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.right

            root = stack.pop()
            count += 1
            if count == k:
                return root.val

            root = root.left
