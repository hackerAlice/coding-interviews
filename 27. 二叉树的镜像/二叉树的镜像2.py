#!/usr/bin/python3

"""
使用迭代方法：通过辅助栈实现
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

        stack = [root]

        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

            node.left, node.right = node.right, node.left

        return root
