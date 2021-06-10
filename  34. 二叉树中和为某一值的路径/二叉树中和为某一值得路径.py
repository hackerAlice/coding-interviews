#!/usr/bin/python3

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:

        path, result = list(), list()

        def backtrack(root, target):
            if not root:
                return

            path.append(root.val)
            target -= root.val
            if not target and not root.left and not root.right:
                result.append(list(path))

            backtrack(root.left, target)
            backtrack(root.right, target)
            path.pop()

        backtrack(root, target)
        return result