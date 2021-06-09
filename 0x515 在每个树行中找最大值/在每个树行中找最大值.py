#!/usr/bin/python3

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = list((root,))
        result = []

        while q:
            result.append(max([node.val for node in q]))
            for _ in range(len(q)):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return result