#!/usr/bin/python3

from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []

        result, q = [], list((root,))

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.pop(0)
                temp.append(node.val)
                if node.children:
                    q.extend(node.children)

            result.append(temp)

        return result
