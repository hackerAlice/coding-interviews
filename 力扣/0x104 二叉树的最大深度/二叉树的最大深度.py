#!/usr/bin/python3

"""
使用深度优先算法来计算
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_hight = self.maxDepth(root.left)
            right_hight = self.maxDepth(root.right)
            return max(left_hight, right_hight) + 1