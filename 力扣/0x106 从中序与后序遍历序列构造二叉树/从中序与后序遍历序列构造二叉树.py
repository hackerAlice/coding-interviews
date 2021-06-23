#!/usr/bin/python3

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])

        inorder_left = inorder[:idx]
        inorder_right = inorder[idx+1:]

        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[-len(inorder_right)-1:-1]

        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        return root