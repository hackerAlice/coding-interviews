#!/usr/bin/python3

"""
使用递归的方法
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        if root.left:
            self.mirrorTree(root.left)

        if root.right:
            self.mirrorTree(root.right)

        return root
