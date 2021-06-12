#!/usr/bin/python

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result, q = list(), list((root,))
        level = 0
        while q:
            temp = []
            level += 1
            for _ in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                result.append(list(temp))
            else:
                result.append(list(temp[::-1]))

        return result