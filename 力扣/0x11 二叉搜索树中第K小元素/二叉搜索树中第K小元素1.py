"""
算法思路：
使用中序遍历转有序数组，直接存取
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return None
        values = []
        self.inorder_travel(root, values)
        if k <= len(values):
            return values[k-1]
        return None

    def inorder_travel(self, root: TreeNode, value_list: List):
        if root:
            self.inorder_travel(root.left, value_list)
            value_list.append(root.val)
            self.inorder_travel(root.right, value_list)