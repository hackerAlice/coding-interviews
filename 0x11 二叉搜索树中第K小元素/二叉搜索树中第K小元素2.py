"""
在递归过程中找出
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    count = 0
    res = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder_travel(root, k)
        return self.res

    def inorder_travel(self, root: TreeNode, k: int):
        if not root:
           return None
        if self.count > k:
            return None

        self.inorder_travel(root.left, k)
        self.count += 1
        if self.count == k:
            self.res += root.val
            return
        self.inorder_travel(root.right, k)