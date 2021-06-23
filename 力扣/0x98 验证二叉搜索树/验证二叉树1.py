#!/usr/bin/python3

"""
根据二叉树的中序遍历是一个严格递增序列来进行判断
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = []

        def inorder(root_node: TreeNode):
            if not root_node:
                return True
            inorder(root_node.left)
            result.append(root_node.val)
            inorder(root_node.right)

        inorder(root)

        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False

        return True