#!/usr/bin/python3

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        q = [root]
        result = []

        while q:
            result.append(q[-1].val)
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
